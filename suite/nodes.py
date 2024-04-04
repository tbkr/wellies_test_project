import pyflow as pf
import wellies as wl


class InitFamily(pf.AnchorFamily):
    def __init__(self, config, **kwargs):
        super().__init__(name='init', **kwargs)
        with self:
            # install environments and packages
            wl.DeployToolsFamily(
                config.tools,
            )

            # setup static data (remote/local copy/link)
            wl.DeployDataFamily(
                config.static_data,
            )


class MainFamily(pf.AnchorFamily):
    def __init__(self, config, **kwargs):
        super().__init__(name='main', **kwargs)
        with self:
            pf.Task(
                name='marsflow_test',
            )


class MarsflowRetrievalFamily(pf.Family):
    def __init__(self, config, **kwargs):
        super().__init__(name='Admin', **kwargs)

        host = pf.TroikaHost(name="fdbdev", user="fdbdev", troika_config="~/troika/config/troika.yml")

        with self:
            pf.Task('marsadm_version', host=host, script='marsadm -command "version -long"')


class MainSuite(pf.Suite):
    def __init__(self, config, **kwargs):

        # add your execution limits here
        limits = {
            'work': 20,
        }

        labels = {
            'info': 'this is the wellies_test_project suite'
        }

        super().__init__(
            limits=limits,
            labels=labels,
            defstatus=pf.state.suspended,
            **kwargs
        )

        limits = {
            k: getattr(self, k) for k in limits.keys()
        }

        with self:
            f_init = InitFamily(config=config, inlimits=self.work)
            f_main = MainFamily(config=config, inlimits=self.work)
            f_main.triggers = f_init.complete
            f_mars = MarsflowRetrievalFamily(config=config, inlimits=self.work)

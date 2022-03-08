from ipywidgets import DOMWidget
from traitlets import Unicode

module_name = 'stl_viewer'
version = '0.1.0'


class STLViewer(DOMWidget):
    _model_name = Unicode('STLViewerModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(version).tag(sync=True)

    _view_name = Unicode('STLViewerView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(version).tag(sync=True)

    value = Unicode('Hello World').tag(sync=True)


def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',  # Must be 'notebook' for widget extensions
        'src': '.',
        'dest': 'stl_viewer',
        'require': 'stl_viewer/stl_viewer'
    }]

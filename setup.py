from distutils.core import Extension, setup

pyctp_module = Extension(
    '_PyCTP',
    sources=['./PyCTP_wrap.cxx'],
    libraries=['thostmduserapi_se', 'thosttraderapi_se']
)

setup(
    name='PyCTP',
    version='0.6.3.16',
    author='xiaohua.hou',
    ext_modules=[pyctp_module],
    py_modules=['PyCTP'],
)

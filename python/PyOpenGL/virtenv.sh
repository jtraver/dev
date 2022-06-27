


# https://pypi.org/project/virtualenv/
# http://pyopengl.sourceforge.net/context/tutorials/shader_intro.html

#virtualenv --sytem-site-packages tutorial
#Johns-MacBook-Pro:PyOpenGL jtraver$ ./virtenv.sh
#usage: virtualenv [--version] [--with-traceback] [-v | -q] [--read-only-app-data] [--app-data APP_DATA] [--reset-app-data] [--upgrade-embed-wheels] [--discovery {builtin}] [-p py] [--try-first-with py_exe]
#                  [--creator {builtin,cpython2-mac-framework}] [--seeder {app-data,pip}] [--no-seed] [--activators comma_sep_list] [--clear] [--no-vcs-ignore] [--system-site-packages] [--symlinks | --copies] [--no-download | --download]
#                  [--extra-search-dir d [d ...]] [--pip version] [--wheel version] [--setuptools version] [--no-pip] [--no-wheel] [--no-setuptools] [--no-periodic-update] [--symlink-app-data] [--prompt prompt] [-h]
#                  dest
#virtualenv: error: unrecognized arguments: --sytem-site-packages
#SystemExit: 2


virtualenv --version

virtualenv tutorial


source tutorial/bin/activate

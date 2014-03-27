# https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager
sudo checkinstall -y --install=no --pkgversion 0.10.26 make -j$(($(nproc)+1)) install
sudo dpkg -i node_*

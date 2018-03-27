#!/usr/bin/env bash

main() {
    source package.rc
    local entries=$(package_packages)
    IFS=$'\n' && for entry in ${entries[@]}; do
        IFS=" " read pkg_repo pkg_kind pkg_os pkg_distro pkg_arch pkg_name pkg_file pkg_url <<< "${entry}"
        pkg_file=$(eval echo $pkg_file)
        pkg_url=$(eval echo $pkg_url)
        pkg_path=${pkg_os/:/}.${pkg_arch}.${pkg_kind}
        #mkdir -p ${pkg_path}
        #run $v "Downloading  ${pkg_url} => ${pkg_path}/${pkg_file}" \
        #    wget -qO ${pkg_path}/${pkg_file} ${pkg_url}
        echo $pkg_repo $pkg_kind $pkg_os=$3 $pkg_distro $pkg_arch $pkg_name $pkg_file $pkg_url $pkg_path
    done
    echo
    local entries=`cat package.txt`
    IFS=$'\n' && for entry in ${entries[@]}; do
        IFS=" " read pkg_repo pkg_kind pkg_os pkg_distro pkg_arch pkg_name pkg_file pkg_url <<< "${entry}"
        pkg_file=$(eval echo $pkg_file)
        pkg_url=$(eval echo $pkg_url)
        pkg_path=${pkg_os/:/}.${pkg_arch}.${pkg_kind}
        #mkdir -p ${pkg_path}
        #run $v "Downloading  ${pkg_url} => ${pkg_path}/${pkg_file}" \
        #    wget -qO ${pkg_path}/${pkg_file} ${pkg_url}
        echo $pkg_repo $pkg_kind $pkg_os=$3 $pkg_distro $pkg_arch $pkg_name $pkg_file $pkg_url $pkg_path
    done
}

main $@

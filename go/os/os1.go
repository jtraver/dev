package main

import (
    "fmt"
    "os"
    "reflect"
    "go/build"
)

func main() {
    fmt.Printf("os\n")
    type1 := reflect.TypeOf(os.Open)
    fmt.Printf("os.Open = %s\n", type1)
    fmt.Printf("os.Open = %v\n", type1)
    value1 := reflect.ValueOf(os.Open)
    fmt.Printf("os.Open = %s\n", value1)
    fmt.Printf("os.Open = %v\n", value1)
    package1, err := build.Import("os", "os", build.AllowBinary)
    if err != nil {
        fmt.Printf("err = %s\n", err)
    } else {
        fmt.Printf("pakage1 = %s\n", package1)
        fmt.Printf("pakage1 = %v\n", package1)
        if package1.IsCommand() {
            fmt.Printf("is command\n")
        } else {
            fmt.Printf("is not command\n")
        }
        type1 := reflect.TypeOf(package1)
        fmt.Printf("package1 = %s\n", type1)
        fmt.Printf("package1 = %v\n", type1)
        for i := 0; i < type1.NumMethod(); i++ {
            method := type1.Method(i)
            fmt.Println(method.Name)
        }
        value1 := reflect.ValueOf(package1)
        fmt.Printf("package1 = %s\n", value1)
        fmt.Printf("package1 = %v\n", value1)
    }
}

/*

package1 = &{/usr/lib/golang/src/os os  Package os provides a platform-independent interface to operating system functionality. os /usr/lib/golang /usr/lib/golang/src /usr/lib/golang/pkg /usr/lib/golang/pkg/linux_amd64 /usr/lib/golang/bin

%!s(bool=true) /usr/lib/golang/pkg/linux_amd64/os.a [darwin dragonfly freebsd linux nacl netbsd openbsd plan9 solaris windows]  
[dir_unix.go
    doc.go
    env.go
    error.go
    error_unix.go
    exec.go
    exec_posix.go
    exec_unix.go
    file.go
    file_posix.go
    file_unix.go
    getwd.go
    path.go
    path_unix.go
    pipe_linux.go
    proc.go
    stat_linux.go
    sticky_notbsd.go
    str.go
    sys_linux.go
    sys_unix.go
    types.go
    types_unix.go]
[]
[dir_plan9.go
    dir_windows.go
    error_plan9.go
    error_windows.go
    exec_plan9.go
    exec_windows.go
    file_plan9.go
    file_windows.go
    getwd_darwin.go
    path_plan9.go
    path_windows.go
    pipe_bsd.go
    stat_darwin.go
    stat_dragonfly.go
    stat_freebsd.go
    stat_nacl.go
    stat_netbsd.go
    stat_openbsd.go
    stat_plan9.go
    stat_solaris.go
    stat_windows.go
    sticky_bsd.go
    sys_bsd.go
    sys_darwin.go
    sys_freebsd.go
    sys_nacl.go
    sys_plan9.go
    sys_solaris.go
    sys_windows.go
    types_plan9.go
    types_windows.go]
[] [] [] [] [] [] [] [] [] [] [] [] [] []
[errors io runtime sync sync/atomic syscall time]
map[errors:[/usr/lib/golang/src/os/error.go:8:2
    /usr/lib/golang/src/os/exec_unix.go:10:2]
    runtime:[/usr/lib/golang/src/os/exec.go:8:2
        /usr/lib/golang/src/os/exec_unix.go:11:2
        /usr/lib/golang/src/os/file_unix.go:10:2
        /usr/lib/golang/src/os/getwd.go:8:2
        /usr/lib/golang/src/os/proc.go:10:2]
    sync/atomic:[/usr/lib/golang/src/os/exec.go:9:2]
    sync:[/usr/lib/golang/src/os/getwd.go:9:2]
    io:[/usr/lib/golang/src/os/dir_unix.go:10:2
        /usr/lib/golang/src/os/file.go:40:2
        /usr/lib/golang/src/os/path.go:8:2]
    syscall:[/usr/lib/golang/src/os/dir_unix.go:11:2
        /usr/lib/golang/src/os/env.go:9:8
        /usr/lib/golang/src/os/error_unix.go:9:8
        /usr/lib/golang/src/os/exec.go:10:2
        /usr/lib/golang/src/os/exec_posix.go:10:2
        /usr/lib/golang/src/os/exec_unix.go:12:2
        /usr/lib/golang/src/os/file.go:41:2
        /usr/lib/golang/src/os/file_posix.go:10:2
        /usr/lib/golang/src/os/file_unix.go:11:2
        /usr/lib/golang/src/os/getwd.go:10:2
        /usr/lib/golang/src/os/path.go:9:2
        /usr/lib/golang/src/os/pipe_linux.go:7:8
        /usr/lib/golang/src/os/proc.go:11:2
        /usr/lib/golang/src/os/stat_linux.go:8:2
        /usr/lib/golang/src/os/types.go:8:2
        /usr/lib/golang/src/os/types_unix.go:11:2]
    time:[/usr/lib/golang/src/os/doc.go:7:8
        /usr/lib/golang/src/os/exec_unix.go:13:2
        /usr/lib/golang/src/os/file_posix.go:11:2
        /usr/lib/golang/src/os/stat_linux.go:9:2
        /usr/lib/golang/src/os/types.go:9:2
        /usr/lib/golang/src/os/types_unix.go:12:2]
]

[] [] map[] [] [] map[]}
*/

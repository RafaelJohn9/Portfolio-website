class libinstall {

    package { 'npm':
        ensure => installed,
    }

    package { 'python3':
        ensure => installed,
    }
}
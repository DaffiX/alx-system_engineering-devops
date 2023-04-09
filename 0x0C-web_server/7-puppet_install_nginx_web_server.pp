class nginx_server {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure => running,
    enable => true,
  }

  file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Hello World!',
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('nginx_server/default.erb'),
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-enabled/default':
    ensure  => 'link',
    target  => '/etc/nginx/sites-available/default',
    require => File['/etc/nginx/sites-available/default'],
    notify  => Service['nginx'],
  }
}

class nginx_redirect {
  file { '/etc/nginx/sites-available/redirect':
    ensure  => file,
    content => template('nginx_server/redirect.erb'),
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-enabled/redirect':
    ensure  => 'link',
    target  => '/etc/nginx/sites-available/redirect',
    require => File['/etc/nginx/sites-available/redirect'],
    notify  => Service['nginx'],
  }
}

include nginx_server
include nginx_redirect


# puppet file for setup

$nginx_conf = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 http://linktr.ee/firdaus_h_salim/;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"

$str = "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

exec { 'update':
command => 'user/bin/apt-get update',
}

package { 'nginx'
ensure   => 'installed',
provider => 'apt',
}

file { '/data/'
ensure => 'directory',
}

file { '/data/web_static/'
ensure => 'directory',
}

file { '/data/web_static/shared/'
ensure => 'directory',
}

file { '/data/web_static/releases/'
ensure => 'directory',
}

file { '/data/web_static/releases/test/'
ensure => 'directory',
}

file { 'index.html':
path    => '/data/web_static/releases/test/',
ensure  => 'present',
content => $str
}

file { '/data/web_static/current':
ensure => link,
target => '/data/web_static/releases/test/'
}

file { '/data/'
ensure => 'directory',
owner  => 'ubuntu',
group  => 'ubuntu',
}

file { '/etc/nginx/sites-enabled/default'
ensure  => 'present',
content => $nginx_conf,
}

service { 'nginx':
ensure => 'running',
enable => true,
}

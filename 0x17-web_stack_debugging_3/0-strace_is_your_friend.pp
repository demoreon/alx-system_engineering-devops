# Fixes bad incorrect `phpp` extensions

file { '/var/www/html/wp-settings.php':
  ensure  => file,
  content => inline_template("<%= File.read('/var/www/html/wp-settings.php').gsub('phpp', 'php') %>"),
}

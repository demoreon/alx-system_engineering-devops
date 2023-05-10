exec { 'fix-wordpress':
  command => '/bin/echo -n "$(cat /var/www/html/wp-settings.php | sed s/phpp/php/g)" > /var/www/html/wp-settings.php',
  }

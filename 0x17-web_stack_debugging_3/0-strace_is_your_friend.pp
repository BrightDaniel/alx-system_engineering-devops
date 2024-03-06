# Create a manifest that fixes file name typo
exec { 'fix_typo':
  command => 'mv /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-locale.phpp',
  path    => '/bin/'
}

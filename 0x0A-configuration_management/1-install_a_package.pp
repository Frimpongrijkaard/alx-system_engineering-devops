# Installs flask
package { 'python3-flask':
  ensure   => '2.5.0',
  provider => pip3,
}

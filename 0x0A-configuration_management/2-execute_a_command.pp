# create a process named killmenow 

exec { 'pkill killmenow' :
    path    => '/bin/',
    command => 'pkill killmenow',
    }

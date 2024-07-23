# Web Stack Debugging

This project contains tasks for learning about how to debug web stacks.

## Tasks To Complete

+ [x] 0. Run software as another user<br/>_**[0-iamsomeoneelse](0-iamsomeoneelse)**_ contains a Bash script that meets the following requirements.
  + Info:
    + The user `root` is, on Linux, the "superuser". It can do anything it wants, that's a good and bad thing. A good practice is that one should never be logged in the `root` user, as if you fat finger a command and for example run `rm -rf /`, there is no comeback. That's why it is preferable to run as a privileged user, meaning that the user also has the ability to perform tasks that the `root` user can do, just need to use a specific command that you need to discover.
    + For the containers that you are given in this project as well as the checker, everything is run under the `root` user, which has the ability to run anything as another user.
  + Requirements:
    + Write a Bash script that accepts one argument.
    + The script should run the `whoami` command under the user passed as an argument.

+ [x] 1. Run Nginx as Nginx<br/>_**[1-fix_in_7_lines_or_less](1-fix_in_7_lines_or_less)**_ contains a Bash script that configures a container to fit the following requirements.
  + Info:
    + The `root` user is a superuser that can do anything on a Unix machine, the top administrator. Security wise, you must do everything that you can to prevent an attacker from logging in as `root`. With this in mind, it's a good practice not to run your web servers as `root` (which is the default for most configurations) and instead run the process as the less privileged nginx user instead. This way, if a hacker does find a security issue that allows them to break-in to your server, the impact is limited by the permissions of the nginx user.
  + Requirements:
    + `nginx` must be running as `nginx` user.
    + `nginx` must be listening on all active IPs on port `8080`.
    + You cannot use `apt-get remove`.

+ [x] 2. 7 lines or less<br/>_**[100-fix_in_7_lines_or_less](100-fix_in_7_lines_or_less)**_ contains a Bash script uses what was done for task #1 but is short and sweet.
  + Requirements:
    + Your Bash script must be 7 lines long or less.
    + There must be a new line at the end of the file.
    + You respect Bash script requirements.
    + You cannot use `;`.
    + You cannot use `&&`.
    + You cannot use `wget`.
    + You cannot execute your previous answer file (Do not include the name of the previous script in this one).

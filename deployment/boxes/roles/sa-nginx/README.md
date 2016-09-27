sa-nginx
========

[![Build Status](https://travis-ci.org/softasap/sa-nginx.svg?branch=master)](https://travis-ci.org/softasap/sa-nginx)


Basic role for nginx based deployments (like MEAN stack)

Adjusts folder structure to be apache style (i.e. sites-available, sites-enabled)

Adjusts hashbucketsize for longer domains.


Example of usage:

<pre>

     - {
         role: "sa-nginx"
       }


</pre>

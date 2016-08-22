====
Page
====


.. blockdiag::
   :desctable:

   blockdiag {
      A -> B -> C;
      A [description = "browsers in each client"];
      B [description = "web server"];
      C [description = "database server"];
   }





.. seqdiag::
   :desctable:

   seqdiag {
      A -> B -> C;
      A [description = "browsers in each client"];
      B [description = "web server"];
      C [description = "database server"];
   }



.. actdiag::
   :desctable:

   actdiag {
      A -> B -> C;
      A [description = "browsers in each client"];
      B [description = "web server"];
      C [description = "database server"];
   }



.. nwdiag::
   :desctable:

   nwdiag {
      network {
        A [address = 192.168.0.1, description = "web server01"];
        B [address = 192.168.0.2, description = "web server02"];
      }
      network {
        A [address = 172.0.0.1];
        C [address = 172.0.0.2, description = "database server"];
      }
   }

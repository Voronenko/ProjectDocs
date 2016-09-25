=======================
Page element's examples
=======================


Blockdiag - block diagram
~~~~~~~~~~~~~~~~~~~~~~~~~

.. blockdiag::
   :desctable:

   blockdiag {
      A -> B -> C;
      A [description = "browsers in each client"];
      B [description = "web server"];
      C [description = "database server"];
   }


Seqdiag - sequence diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~


.. seqdiag::
   :desctable:

   seqdiag {
      A -> B -> C;
      A [description = "browsers in each client"];
      B [description = "web server"];
      C [description = "database server"];
   }


Actdiag - activity diagrams
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. actdiag::
   :desctable:

   actdiag {
      A -> B -> C;
      A [description = "browsers in each client"];
      B [description = "web server"];
      C [description = "database server"];
   }


nwdiag - network diagram
~~~~~~~~~~~~~~~~~~~~~~~~

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


Plantuml
~~~~~~~~

.. uml::

   @startuml
   user -> (use PlantUML)

   note left of user
      Hello!
   end note
   @enduml




.. uml::

   @startuml
   Alice -> Bob: Hi!
   Alice <- Bob: How are you?
   @enduml


Plantuml - class diagrams
~~~~~~~~~~~~~~~~~~~~~~~~~


.. uml::

      @startuml

      'style options
      skinparam monochrome true
      skinparam circledCharacterRadius 0
      skinparam circledCharacterFontSize 0
      skinparam classAttributeIconSize 0
      hide empty members

      Class01 <|-- Class02
      Class03 *-- Class04
      Class05 o-- Class06
      Class07 .. Class08
      Class09 -- Class10

      @enduml



.. uml::

      @startuml

      'style options
      skinparam monochrome true
      skinparam circledCharacterRadius 0
      skinparam circledCharacterFontSize 0
      skinparam classAttributeIconSize 0
      hide empty members

      class Car

      Driver - Car : drives >
      Car *- Wheel : have 4 >
      Car -- Person : < owns

      @enduml





.. uml::

      @startuml

      'style options
      skinparam monochrome true
      skinparam circledCharacterRadius 0
      skinparam circledCharacterFontSize 0
      skinparam classAttributeIconSize 0
      hide empty members

      class Car

      Driver - Car : drives >
      Car *- Wheel : have 4 >
      Car -- Person : < owns

      @enduml


To declare fields and methods, you can use the symbol ”:” followed by the field’s or method’s name. The system checks for parenthesis to choose between methods and fields.

.. uml::

      @startuml

      'style options
      skinparam monochrome true
      skinparam circledCharacterRadius 9
      skinparam circledCharacterFontSize 8
      skinparam classAttributeIconSize 0
      hide empty members

      abstract class AbstractClass {
        - privateField
        + publicField
        # protectedField
        ~ packagePrivateField
        - privateMethod()
        + publicMethod()
        # protectedMethod()
        ~ packagePrivateMethod()
         }

      class Dummy {
        {static} staticID
        {abstract} void methods()
         }

      class Flight {
         flightNumber : Integer
         departureTime : Date
         }

      package "Classic Collections" {

         abstract class AbstractList
         abstract AbstractCollection
         interface List
         interface Collection

         List <|-- AbstractList
         Collection <|-- AbstractCollection

         Collection <|- List
         AbstractCollection <|- AbstractList
         AbstractList <|-- ArrayList

         class ArrayList {
           Object[] elementData
           size()
            }
      }

      enum TimeUnit {
        DAYS
        HOURS
        MINUTES
      }


      class Student {
        Name
      }
      Student "0..*" -- "1..*" Course
      (Student, Course) .. Enrollment

      class Enrollment {
        drop()
        cancel()
      }

      @enduml


Plantuml - usecase diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~


.. uml::

   @startuml
   actor "Main Database" as DB << Application >>

   note left of DB
      This actor
      has a "name with spaces",
      an alias
      and a stereotype
   end note

   actor User << Human >>
   actor SpecialisedUser
   actor Administrator

   User <|--- SpecialisedUser
   User <|--- Administrator

   usecase (Use the application) as (Use) << Main >>
   usecase (Configure the application) as (Config)
   Use ..> Config : <<includes>>

   User --> Use
   DB --> Use

   Administrator --> Config

   note "This note applies to\nboth actors." as MyNote
   MyNote .. Administrator
   MyNote .. SpecialisedUser

   '  this is a text comment and won't be displayed
   AnotherActor ---> (AnotherUseCase)

   '  to increase the length of the edges, just add extras dashes, like this:
   ThirdActor ----> (LowerCase)

   '  The direction of the edge can also be reversed, like this:
   (UpperCase) <---- FourthActor

   @enduml


Plantuml - activity diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. uml::

   @startuml

   start

   :first activity;

   :second activity
    with a multiline
    and rather long description;

   :another activity;

   note right
     After this activity,
     are two 'if-then-else' examples.
   end note

   if (do optional activity?) then (yes)
      :optional activity;
   else (no)

      if (want to exit?) then (right now!)
         stop
      else (not really)

      endif

   endif

   :third activity;

   note left
     After this activity,
     parallel activities will occur.
   end note

   fork
      :Concurrent activity A;
   fork again
      :Concurrent activity B1;
      :Concurrent activity B2;
   fork again
      :Concurrent activity C;
      fork
      :Nested C1;
      fork again
      :Nested C2;
      end fork
   end fork

   repeat
      :repetitive activity;
   repeat while (again?)

   while (continue?) is (yes, of course)
     :first activity inside the while loop;
     :second activity inside the while loop;
   endwhile (no)

   stop

   @enduml


Plantuml - state diagram
~~~~~~~~~~~~~~~~~~~~~~~~


.. uml::

   @startuml

   [*] --> MyState
   MyState --> CompositeState
   MyState --> AnotherCompositeState
   MyState --> WrongState

   CompositeState --> CompositeState : \ this is a loop
   AnotherCompositeState --> [*]
   CompositeState --> [*]

   MyState : this is a string
   MyState : this is another string

   state CompositeState {

   [*] --> StateA : begin something
   StateA --> StateB : from A to B
   StateB --> StateA : from B back to A
   StateB --> [*] : end it

   CompositeState : yet another string
   }

   state AnotherCompositeState {

   [*] --> ConcurrentStateA
   ConcurrentStateA --> ConcurrentStateA

   --

   [*] --> ConcurrentStateB
   ConcurrentStateB --> ConcurrentStateC
   ConcurrentStateC --> ConcurrentStateB
   }

   note left of WrongState
      This state
      is a dead-end
      and shouldn't
      exist.
   end note

   @enduml


Plantuml - UI example
~~~~~~~~~~~~~~~~~~~~~

.. uml::

   @startuml
   salt
   {
     Just plain text
     [This is my button]
     ()  Unchecked radio
     (X) Checked radio
     []  Unchecked box
     [X] Checked box
     "Enter text here   "
     ^This is a droplist^
   }
   @enduml

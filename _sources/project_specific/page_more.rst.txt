More examples
#############

Activity diagrams
~~~~~~~~~~~~~~~~~

.. begin-activity-diagram-example

.. uml::

    @startuml

    title Activity Diagram \n

    start

    :Eat Hot Wings;

    note left
        This is a Note...
        * Activity diagrams can begin with a Start
        * An activity is colon, some words, and a semicolon
        * Activity diagrams can end with a stop
    end note

    :Drink Homebrew;

    stop

    @enduml

.. end-activity-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
  :language: rst
  :start-after: begin-activity-diagram-example
  :end-before: end-activity-diagram-example

.. begin-conditional-activity-diagram-example

.. uml::

    @startuml

    title Conditional - Activity Diagram


    start

    :Eat Hot Wings;
    note right: This is a note to the right

    :Drink Homebrew;
    note left: This is a note to the left

    if (Turn On The Game?) then (yes)
    :__Having Fun__!!!;
    else (no)
    :Not Having Fun;
    endif

    :Go To Bed;

    stop

    @enduml

.. end-conditional-activity-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
      :language: rst
      :start-after: begin-conditional-activity-diagram-example
      :end-before: end-conditional-activity-diagram-example


.. begin-notes-activity-diagram-example

.. uml::

    @startuml

    title Notes - Activity Diagram


    start

    :Eat Hot Wings;

    note right
    This note is on several lines
    ....
    //This line is in italics//
    ----
    This one contains som <b>HTML</b>
    ====
    * This line contains a bullet
    ____
    "" This line is in code block""
    end note

    :Drink Homebrew;

    stop

    @enduml

.. end-notes-activity-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
        :language: rst
        :start-after: begin-notes-activity-diagram-example
        :end-before: end-notes-activity-diagram-example


.. begin-repeat-activity-diagram-example

.. uml::

    @startuml

    title Repeat - Activity Diagram


    start

    repeat
    :Eat Hot Wings;
    :Drink Homebrew;
    repeat while (Still Hungry?)

    stop

    @enduml

.. end-repeat-activity-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-repeat-activity-diagram-example
          :end-before: end-repeat-activity-diagram-example


.. begin-while-activity-diagram-example

.. uml::

    @startuml

    title While Loop - Activity Diagram


    start

    while (Hungry?)  is (Yes)
    :Eat Hot Wings;
    :Drink Homebrew;
    endwhile (No)

    :Go To Sleep;

    stop

    @enduml

.. end-while-activity-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-while-activity-diagram-example
          :end-before: end-while-activity-diagram-example

.. begin-parallel-activity-diagram-example

.. uml::

    @startuml

    title Parallel - Activity Diagram


    start

    :Eat Hot Wings;

    :Drink Homebrew;

    if (Turn On The Game?) then (yes)
    fork
        :__Having Fun__!!!;
    fork again
        :Scream At TV!!;
    end fork
    else (no)
    :Not Having Fun;
    :Eat Poptart;
    endif

    :Go To Bed;

    stop

    @enduml

.. end-parallel-activity-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-parallel-activity-diagram-example
          :end-before: end-parallel-activity-diagram-example


.. begin-color-activity-diagram-example

.. uml::

    @startuml

    title Color - Activity Diagram


    skinparam backgroundColor #AAAAAA
    skinparam activity {
    StartColor Blue
    EndColor Red
    BackgroundColor Green
    BorderColor Yellow
    }

    start

    :Eat Hot Wings;

    :Drink Homebrew;

    stop

    @enduml

.. end-color-activity-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-color-activity-diagram-example
          :end-before: end-color-activity-diagram-example



Class diagrams
~~~~~~~~~~~~~~


.. begin-classes-class-diagram-example

.. uml::

    @startuml

    title Classes - Class Diagram


    class Dwelling {
    +Int Windows
    +void Lock()
    }

    class Apartment
    class House
    class Commune

    @enduml

.. end-classes-class-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-classes-class-diagram-example
          :end-before: end-classes-class-diagram-example


.. begin-relationships-class-diagram-example

.. uml::

    @startuml

    title Relationships - Class Diagram


    class Dwelling {
    +Int Windows
    +void LockTheDoor()
    }

    class Apartment
    class House
    class Commune
    class Window
    class Door

    Dwelling <|-down- Apartment: Inheritance
    Dwelling <|-down- Commune: Inheritance
    Dwelling <|-down- House: Inheritance
    Dwelling "1" *-up- "many" Window: Composition
    Dwelling "1" *-up- "many" Door: Composition

    @enduml


.. end-relationships-class-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-relationships-class-diagram-example
          :end-before: end-relationships-class-diagram-example


.. begin-types-class-diagram-example


.. uml::

    @startuml

    title Types - Class Diagram


    skinparam componentStyle uml2

    abstract class AbstractList {

    }

    class Test << general >> {
    }

    class System << (S,#FF7700) Singleton >>
    class Date << (D,orchid) >>

    class Foo1<Generics tag> {
    You can use
    several lines
    ..
    as you want
    and group
    ==
    things together.
    __
    You can have as many groups
    as you want
    --
    End of class
    }

    class User {
    .. Simple Getter ..
    + getName() : String
    + getAddress() : Address
    .. Some setter ..
    + setName() : String
    __ private data __
    -int age
    -- crypted --
    -String password
    }

    enum TimeUnit {
    DAYS
    HOURS
    MINUTES
    }

    interface List {

    }

    annotation SuppressWarnings

    class Object << general >>
    Object <|--- ArrayList

    @enduml


.. end-types-class-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-types-class-diagram-example
          :end-before: end-types-class-diagram-example


.. begin-methods-class-diagram-example

.. uml::

    @startuml

    title Properties / Methods - Class Diagram


    skinparam componentStyle uml2
    class Car {
    .. Field Examples ..
    - Name: Type { arg1, arg2, argn }
    +Name: Type { arg1, arg2, argn }
    #Name: Type { arg1, arg2, argn }
    ~Name: Type { arg1, arg2, argn }

    .. Method Examples ..
    -Name(): Type { arg1, arg2, argn }
    +Name(): Type { arg1, arg2, argn }
    #Name(): Type { arg1, arg2, argn }
    ~Name(): Type { arg1, arg2, argn }

    .. Static Example ..
    +{static} Name(): Type { arg1, arg2, argn }

    .. Abstract Example ..
    +{abstract} Name(): Type { arg1, arg2, argn }
    }

    class Car
    ICar ()- Car
    ICar2 ()-- Car
    Car -() ICar3

    @enduml

.. end-methods-class-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-methods-class-diagram-example
          :end-before: end-methods-class-diagram-example


.. begin-interfaces-class-diagram-example

.. uml::

    @startuml

    title Interfaces - Class Diagram


    class Car
    ICar ()- Car
    ICar2 ()-- Car
    Car -() ICar3

    @enduml

.. end-interfaces-class-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-interfaces-class-diagram-example
          :end-before: end-interfaces-class-diagram-example


.. begin-packages-class-diagram-example

.. uml::

    @startuml

    title Packages - Class Diagram


    package Node <<Node>> {
    class Worker1
    }

    package Rectangle <<Rect>> {
    class Worker2
    }

    package Folder <<Folder>> {
    class Worker3
    }

    package Frame <<Frame>> {
    class Worker4
    }

    package Internet <<Cloud>> {
    class Worker5
    }

    package Database <<Database>> {
    class Worker6
    }

    @enduml

.. end-packages-class-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-packages-class-diagram-example
          :end-before: end-packages-class-diagram-example


Component diagrams
~~~~~~~~~~~~~~~~~~

.. begin-components-component-diagram-example

.. uml::

    @startuml

    title Components - Component Diagram

    [Business Logic]
    [Data Access] as DA
    component [Graphic User\nInterface] as GUI

    @enduml


.. end-components-component-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-components-component-diagram-example
          :end-before: end-components-component-diagram-example


.. begin-interfaces-component-diagram-example

.. uml::

    @startuml

    title Interfaces - Component Diagram

    [Business Logic]
    [Data Access] as DA
    component [Graphic User\nInterface] as GUI

    interface IMath as Math
    interface "IItems" as Items

    [Business Logic] -- Math
    DA .. Items

    @enduml

.. end-interfaces-component-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-interfaces-component-diagram-example
          :end-before: end-interfaces-component-diagram-example


.. begin-packages-component-diagram-example

.. uml::

    @startuml

    skinparam componentStyle uml2

    title Packages - Component Diagram

    package "Front End" {
        component [Graphic User\nInterface] as GUI
    }

    cloud Internet {
    }

    node "Middle Tier" {
        [Business Logic]
        [Data Access] as DA
        interface IMath as Math
        note left of Math : This is a web\nService Interface
        note right of Math : Notice the\nlabel below
        interface "IItems" as Items

        note left of [Business Logic]
            A note can also
            be on several lines
            like this one
        end note

    }

    database "PostgreSQL\n" {
        [Stored Procs]
    }

    GUI -down-> Internet
    Internet -down-( Math
    [Business Logic] -up- Math : Web Services
    DA -up- Items  : .Net
    [Business Logic] --( Items
    DA .. [Stored Procs]

    @enduml

.. end-packages-component-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-packages-component-diagram-example
          :end-before: end-packages-component-diagram-example


Graphviz diagrams
~~~~~~~~~~~~~~~~~

Hello world


.. begin-hello-gv-diagram-example

.. uml::

    @startuml
    digraph G {
        Hello -> World
    }
    @enduml

.. end-hello-gv-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-hello-gv-diagram-example
          :end-before: end-hello-gv-diagram-example


.. begin-world-gv-diagram-example

World dynamics

.. uml::

    @startuml
    digraph world {
    size="7,7";
        {rank=same; S8 S24 S1 S35 S30;}
        {rank=same; T8 T24 T1 T35 T30;}
        {rank=same; 43 37 36 10 2;}
        {rank=same; 25 9 38 40 13 17 12 18;}
        {rank=same; 26 42 11 3 33 19 39 14 16;}
        {rank=same; 4 31 34 21 41 28 20;}
        {rank=same; 27 5 22 32 29 15;}
        {rank=same; 6 23;}
        {rank=same; 7;}

        S8 -> 9;
        S24 -> 25;
        S24 -> 27;
        S1 -> 2;
        S1 -> 10;
        S35 -> 43;
        S35 -> 36;
        S30 -> 31;
        S30 -> 33;
        9 -> 42;
        9 -> T1;
        25 -> T1;
        25 -> 26;
        27 -> T24;
        2 -> {3 ; 16 ; 17 ; T1 ; 18}
        10 -> { 11 ; 14 ; T1 ; 13; 12;}
        31 -> T1;
        31 -> 32;
        33 -> T30;
        33 -> 34;
        42 -> 4;
        26 -> 4;
        3 -> 4;
        16 -> 15;
        17 -> 19;
        18 -> 29;
        11 -> 4;
        14 -> 15;
        37 -> {39 ; 41 ; 38 ; 40;}
        13 -> 19;
        12 -> 29;
        43 -> 38;
        43 -> 40;
        36 -> 19;
        32 -> 23;
        34 -> 29;
        39 -> 15;
        41 -> 29;
        38 -> 4;
        40 -> 19;
        4 -> 5;
        19 -> {21 ; 20 ; 28;}
        5 -> {6 ; T35 ; 23;}
        21 -> 22;
        20 -> 15;
        28 -> 29;
        6 -> 7;
        15 -> T1;
        22 -> T35;
        22 -> 23;
        29 -> T30;
        7 -> T8;
        23 -> T24;
        23 -> T1;
    }
    @enduml


.. end-world-gv-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-world-gv-diagram-example
          :end-before: end-world-gv-diagram-example



Data structures

.. begin-data-gv-diagram-example

.. uml::

    @startuml
    digraph g {
    graph [
    rankdir = "LR"
    ];
    node [
    fontsize = "16"
    shape = "ellipse"
    ];
    edge [
    ];
    "node0" [
    label = "<f0> 0x10ba8| <f1>"
    shape = "record"
    ];
    "node1" [
    label = "<f0> 0xf7fc4380| <f1> | <f2> |-1"
    shape = "record"
    ];
    "node2" [
    label = "<f0> 0xf7fc44b8| | |2"
    shape = "record"
    ];
    "node3" [
    label = "<f0> 3.43322790286038071e-06|44.79998779296875|0"
    shape = "record"
    ];
    "node4" [
    label = "<f0> 0xf7fc4380| <f1> | <f2> |2"
    shape = "record"
    ];
    "node5" [
    label = "<f0> (nil)| | |-1"
    shape = "record"
    ];
    "node6" [
    label = "<f0> 0xf7fc4380| <f1> | <f2> |1"
    shape = "record"
    ];
    "node7" [
    label = "<f0> 0xf7fc4380| <f1> | <f2> |2"
    shape = "record"
    ];
    "node8" [
    label = "<f0> (nil)| | |-1"
    shape = "record"
    ];
    "node9" [
    label = "<f0> (nil)| | |-1"
    shape = "record"
    ];
    "node10" [
    label = "<f0> (nil)| <f1> | <f2> |-1"
    shape = "record"
    ];
    "node11" [
    label = "<f0> (nil)| <f1> | <f2> |-1"
    shape = "record"
    ];
    "node12" [
    label = "<f0> 0xf7fc43e0| | |1"
    shape = "record"
    ];
    "node0":f0 -> "node1":f0 [
    id = 0
    ];
    "node0":f1 -> "node2":f0 [
    id = 1
    ];
    "node1":f0 -> "node3":f0 [
    id = 2
    ];
    "node1":f1 -> "node4":f0 [
    id = 3
    ];
    "node1":f2 -> "node5":f0 [
    id = 4
    ];
    "node4":f0 -> "node3":f0 [
    id = 5
    ];
    "node4":f1 -> "node6":f0 [
    id = 6
    ];
    "node4":f2 -> "node10":f0 [
    id = 7
    ];
    "node6":f0 -> "node3":f0 [
    id = 8
    ];
    "node6":f1 -> "node7":f0 [
    id = 9
    ];
    "node6":f2 -> "node9":f0 [
    id = 10
    ];
    "node7":f0 -> "node3":f0 [
    id = 11
    ];
    "node7":f1 -> "node1":f0 [
    id = 12
    ];
    "node7":f2 -> "node8":f0 [
    id = 13
    ];
    "node10":f1 -> "node11":f0 [
    id = 14
    ];
    "node10":f2 -> "node12":f0 [
    id = 15
    ];
    "node11":f2 -> "node1":f0 [
    id = 16
    ];
    }
    @enduml


.. end-data-gv-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-data-gv-diagram-example
          :end-before: end-data-gv-diagram-example


Graph cluster node gradient

.. begin-gradient-gv-diagram-example

.. uml::

    @startuml
    digraph G {
    bgcolor="purple:pink" label="agraph" fontcolor="white"
    subgraph cluster1 {fillcolor="blue:cyan" label="acluster" fontcolor="white" style="filled" gradientangle="270"
            node [shape=box fillcolor="red:yellow" style="filled" gradientangle=90]
            anode;
        }

    }
    @enduml

.. end-gradient-gv-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-gradient-gv-diagram-example
          :end-before: end-gradient-gv-diagram-example



Object diagrams
~~~~~~~~~~~~~~~

.. begin-objects-object-diagram-example

.. uml::

    @startuml

    title Simple Object Diagram

    object Germany
    object France
    object Spain
    object USA
    object Mexico
    object Russia
    object Canada
    object Japan

    Germany <|-- France
    Spain *-- USA
    Mexico o-- Russia
    Canada .. Japan

    Germany : Liquor = Jagermeister
    France : Liquor = Wine
    Spain : Liquor = Wine
    USA : Liquor = BudLight
    Mexico : Liquor = Taquilla
    Russia : Liquor = Vodka
    Canada : Liquor = Beer
    Japan : Liquor = Sake

    @enduml

.. end-objects-object-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-objects-object-diagram-example
          :end-before: end-objects-object-diagram-example


Salt gui diagrams
~~~~~~~~~~~~~~~~~

Basic elements

.. begin-basic-salt-diagram-example

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
    "This is a textbox   "
    ^This is a droplist^
    }

    @enduml

.. end-basic-salt-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-basic-salt-diagram-example
          :end-before: end-basic-salt-diagram-example


Grid


.. begin-grid-salt-diagram-example

.. uml::

    @startsalt

    {
    User Name:| "Justin     "
    Password: | "****       "
    [Ok    ]  | [  Close   ]
    }

    @endsalt

.. end-grid-salt-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-grid-salt-diagram-example
          :end-before: end-grid-salt-diagram-example


Separators

.. begin-separators-salt-diagram-example

.. uml::

    @startsalt

    {
    This is a dotted line
    ..
    This is a double line
    ==
    This is a thick solid line
    ~~
    This is a thin solid line
    --
    }

    @endsalt

.. end-separators-salt-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-separators-salt-diagram-example
          :end-before: end-separators-salt-diagram-example


Treeview


.. begin-tree-salt-diagram-example

.. uml::

    @startsalt

    {
        {T
        + Food
        ++ Fruit
        +++ Grape
        +++ Orange
        +++ Apple
        ++++ Honey Crisp
        ++++ Granny Smith
        +++ Banana
        ++ Vegetables
        +++ Bell pepper
        +++ Spinach
        +++ Mushroom
        ++++ Crimini
        ++++ Shitaki
        }
    }

    @endsalt

.. end-tree-salt-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-tree-salt-diagram-example
          :end-before: end-tree-salt-diagram-example


Brackets

.. begin-brackets-salt-diagram-example

.. uml::

    @startsalt

    {
    Name         | "                 "
    Direction:   | { (X) Left | () Right | () Up | () Down }
    Attending?:  | {  [] Yes | [] No
                    [] Maybe }
    [Browse...] }
    }

    @endsalt

.. end-brackets-salt-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-brackets-salt-diagram-example
          :end-before: end-brackets-salt-diagram-example


Tabs

.. begin-tabs-salt-diagram-example

.. uml::

    @startsalt

    {+

        {/ <b>General | Fullscreen | Behavior | Saving }

        {
        Name         | "                 "
        Direction:   | { (X) Left | () Right | () Up | () Down }
        Attending?:  | {  [] Yes | [] No
                        [] Maybe }
        [Browse...] }
        }

    }

    @endsalt

.. end-tabs-salt-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-tabs-salt-diagram-example
          :end-before: end-tabs-salt-diagram-example


Menus

.. begin-menus-salt-diagram-example

.. uml::

    @startsalt

    {+

    {* File | Edit | Source | Refactor
    Refactor | New | Open File | - | Close | <b>Close All</b> }

        {/ <b>General | Fullscreen | Behavior | Saving }

        {
        Name         | "                 "
        Direction:   | { (X) Left | () Right | () Up | () Down }
        Attending?:  | {  [] Yes | [] No
                        [] Maybe }
        [Browse...] }
        }

    }

    @endsalt

.. end-menus-salt-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-menus-salt-diagram-example
          :end-before: end-menus-salt-diagram-example


Sequence diagrams
~~~~~~~~~~~~~~~~~

.. begin-parts-sequence-diagram-example

.. uml::

    @startuml

    title "Participants - Sequence Diagram"

    actor User
    boundary "Web GUI" as GUI
    control "Shopping Cart" as SC
    entity Widget
    database Widgets

    @enduml

.. end-parts-sequence-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-parts-sequence-diagram-example
          :end-before: end-parts-sequence-diagram-example


.. begin-messages-sequence-diagram-example

.. uml::

    @startuml

    title "Messages - Sequence Diagram"

    actor User
    boundary "Web GUI" as GUI
    control "Shopping Cart" as SC
    entity Widget
    database Widgets

    User -> GUI : To boundary
    GUI -> SC : To control
    SC -> Widget : To entity
    Widget -> Widgets : To database

    @enduml

.. end-messages-sequence-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-messages-sequence-diagram-example
          :end-before: end-messages-sequence-diagram-example


.. begin-comments-sequence-diagram-example

.. uml::

    @startuml

    title "Comments - Sequence Diagram"

    'This is a single line comment

    /'
    This is a multi-
    line comment
    '/

    actor User
    boundary "Web GUI" as GUI
    control "Shopping Cart" as SC
    entity Widget
    database Widgets

    User -> GUI : To boundary
    GUI -> SC : To control
    SC -> Widget : To entity
    Widget -> Widgets : To database

    @enduml

.. end-comments-sequence-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-comments-sequence-diagram-example
          :end-before: end-comments-sequence-diagram-example


.. begin-message-sequence-diagram-example

.. uml::

    @startuml

    title Message Style - Sequence Diagram

    Bob -> Alice
    Bob ->> Alice
    Bob -\ Alice
    Bob \- Alice
    Bob //-- Alice

    Bob ->o Alice
    Bob o\-- Alice

    Bob <-> Alice
    Bob <->o Alice

    @enduml

.. end-message-sequence-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-message-sequence-diagram-example
          :end-before: end-message-sequence-diagram-example


State diagrams
~~~~~~~~~~~~~~

.. begin-states-state-diagram-example

.. uml::

    @startuml

    title Simple State Model
    [*] --> GlassEmpty
    GlassEmpty --> [*]
    GlassEmpty : Contents - void

    GlassEmpty -> GlassFull
    GlassFull : Water
    GlassFull --> [*]

    note right
    this is a note
    end note

    @enduml

.. end-states-state-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-states-state-diagram-example
          :end-before: end-states-state-diagram-example

.. begin-composite-state-diagram-example

.. uml::

    @startuml

    title Simple Composite State Model
    [*] --> NeilDiamond
    state NeilDiamond

    state "Neil Diamond" as NeilDiamond {
    state Dancing
    state Singing
    state Smiling
    Dancing --> Singing
    Singing --> Smiling
    Smiling --> Dancing
    }

    @enduml

.. end-composite-state-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-composite-state-diagram-example
          :end-before: end-composite-state-diagram-example

.. begin-orto-state-diagram-example

.. uml::

    @startuml
    title Simple Orthogonal Composite State Model
    [*] --> NeilDiamond
    state NeilDiamond

    state "Neil Diamond Onstage" as NeilDiamond {
    state Dancing
    state Singing
    state Smiling
    Dancing --> Singing
    Singing --> Smiling
    Smiling --> Dancing
    }

    state NDoff
    state "Neil Diamond in Dressing Room" as NDoff {
    state ThinkingAboutAmerica
    state WatchingGlee
    ThinkingAboutAmerica --> WatchingGlee
    WatchingGlee --> ThinkingAboutAmerica
    }

    NeilDiamond -Right-> NDoff : Walking
    NDoff -Left-> NeilDiamond :Running

    @enduml

.. end-orto-state-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-orto-state-diagram-example
          :end-before: end-orto-state-diagram-example


.. begin-concurrent-state-diagram-example

.. uml::

    @startuml

    Title Concurrent State - C3PO
    [*] --> InDanger
    State "In Danger" as InDanger {
    [*] -> Worrying
    Worrying --> Complaining
    Complaining --> Worrying
    --
    state "Having Illusions of Grandeur" as grandeur
    state "Calculating Odds of Survival" as survival
    [*] -> grandeur
    grandeur --> survival
    survival --> grandeur
    --
    state "Being Prissy" as prissy
    state "Hating Chewbacca" as chewbacca
    [*] -> prissy
    prissy --> chewbacca
    chewbacca --> prissy
    }

    @enduml

.. end-concurrent-state-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-concurrent-state-diagram-example
          :end-before: end-concurrent-state-diagram-example

.. begin-arrows-state-diagram-example

.. uml::

    @startuml

    Title Arrows and Notes
    State Hungry
    State "Eating Burrito" as EatingBurrito
    State Full
    State Sleeping

    note left of Hungry : Single line note
    note right of EatingBurrito
        Notes can also
        take up multiple
        lines like this
    end note

    Hungry -right-> EatingBurrito
    EatingBurrito -down-> Full
    Full -left-> Sleeping
    Sleeping -up-> Hungry

    @enduml

.. end-arrows-state-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-arrows-state-diagram-example
          :end-before: end-arrows-state-diagram-example


Use case diagrams
~~~~~~~~~~~~~~~~~

.. begin-use-uc-diagram-example

.. uml::

    @startuml

    title Use Case Diagram


    (Login)
    (Run Process) as (Proc1)
    usecase (Undo Process)
    usecase (Log Out) as UC4

    @enduml

.. end-use-uc-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-use-uc-diagram-example
          :end-before: end-use-uc-diagram-example

.. begin-actors-uc-diagram-example

.. uml::

    @startuml

    title Actors - Use Case Diagram


    :Administrator:
    :Standard User: as SU
    actor Accountant
    actor :Client: as C

    @enduml

.. end-actors-uc-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-actors-uc-diagram-example
          :end-before: end-actors-uc-diagram-example

.. begin-actors-uc-diagram-example-2


.. uml::

    @startuml

    Employee -up-|> User
    Client -up-|> User
    Supervisor -up-|> User
    Employee --> (Login)
    Supervisor --> (Login)
    Client ..> (Login) : NO!!!!
    Supervisor --> (Create / Delete User): I am god

    @enduml

.. end-actors-uc-diagram-example-2

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-actors-uc-diagram-example-2
          :end-before: end-actors-uc-diagram-example-2

.. begin-stereotypes-uc-diagram-example

.. uml::

    @startuml

    title Stereotypes - Use Case Diagram


    (Login) as L
    (Upload File) as UF<<Manual>>
    actor :User: as U<<Person>>
    :HAL: as H<<Computer>>

    U -> UF
    U ---> (L)
    H <.up.> (L)

    @enduml

.. end-stereotypes-uc-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-stereotypes-uc-diagram-example
          :end-before: end-stereotypes-uc-diagram-example


.. begin-directions-uc-diagram-example

.. uml::

    @startuml

    title Directions - Use Case Diagram

    actor :Admin: as A

    A -> (Login)
    A --> (Logout)
    A -left-> (Copy / Paste)
    A -up-> (Bulk Upload)
    A ---> (Throw Computer Out Of Window!!!)

    @enduml

.. end-directions-uc-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-directions-uc-diagram-example
          :end-before: end-directions-uc-diagram-example


.. begin-package-uc-diagram-example

.. uml::

    @startuml

    title Package - Use Case Diagram


    rectangle Features {
        (Login)
        (Create / Delete User) as CDU
    }

    :Employee:
    :Client:
    :Supervisor:

    Employee --> (Login)
    Supervisor --> (Login)
    Client ..> (Login) : NO!!!!
    Supervisor ---> CDU: I am god

    @enduml

.. end-package-uc-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-package-uc-diagram-example
          :end-before: end-package-uc-diagram-example



XEarth
~~~~~~

Basic

.. begin-xearth-xearth-diagram-example

.. uml::

    @startuml
    xearth
    @enduml

.. end-xearth-xearth-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-xearth-xearth-diagram-example
          :end-before: end-xearth-xearth-diagram-example

.. begin-denver-xearth-diagram-example

.. uml::

    @startuml
    xearth(600,600)
    viewMagnification = 1.0
    daySideBrightness = 100
    nightSideBrightness = 50
    terminatorDiscontinuity = 30
    sunPosRelLong = -40
    sunPosRelLat = 20
    39.75 -105.00 "Denver"
    @enduml

.. end-denver-xearth-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-denver-xearth-diagram-example
          :end-before: end-denver-xearth-diagram-example


.. begin-stars-xearth-diagram-example

.. uml::

    @startuml
    xearth(300,300)
    starsP = true
    starFrequency = 0.025
    bigStars = 20
    @enduml

.. end-stars-xearth-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-stars-xearth-diagram-example
          :end-before: end-stars-xearth-diagram-example


.. begin-stars-xearth-diagram-example-2

.. uml::

    @startuml
    xearth(300,300)
    viewPositionType = Sun-relative
    sunPosRelLat = -10
    sunPosRelLong = 40
    @enduml

.. end-stars-xearth-diagram-example-2

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-stars-xearth-diagram-example-2
          :end-before: end-stars-xearth-diagram-example-2


.. begin-stars-xearth-diagram-example-3

.. uml::

    @startuml
    xearth(300,300)
    gridP = true
    gridDivision = 9
    gridPixelDivision = 8
    @enduml

.. end-stars-xearth-diagram-example-3

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-stars-xearth-diagram-example-3
          :end-before: end-stars-xearth-diagram-example-3


.. begin-stars-xearth-diagram-example-4

.. uml::

    @startuml
    xearth(300,300)
    viewPositionType = Fixed
    viewPosLat = -30
    viewPosLong = -30
    shadeP = false
    gridP = false
    @enduml

.. end-stars-xearth-diagram-example-4

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-stars-xearth-diagram-example-4
          :end-before: end-stars-xearth-diagram-example-4


.. begin-moon-xearth-diagram-example

.. uml::

    @startuml
    xearth(300,300)
    viewPositionType = Moon
    daySideBrightness = 100
    nightSideBrightness = 30
    terminatorDiscontinuity = 50
    @enduml

.. end-moon-xearth-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :start-after: begin-moon-xearth-diagram-example
          :end-before: end-moon-xearth-diagram-example


.. begin-cities-xearth-diagram-example

.. uml::

    @startuml
    xearth
    61.17 -150.00 "Anchorage"           # Alaska, USA
    38.00   23.73 "Athens"              # Greece
    33.4    44.4  "Baghdad"             # Iraq
    13.73  100.50 "Bangkok"             # Thailand
    39.92  116.43 "Beijing"             # China
    52.53   13.42 "Berlin"              # Germany
    32.3   -64.7  "Bermuda"             # Bermuda
    42.33  -71.08 "Boston"              # Massachusetts, USA
    -15.8   -47.9  "Brasilia"            # Brazil
    -4.2    15.3  "Brazzaville"         # Congo
    -34.67  -58.50 "Buenos Aires"        # Argentina
    31.05   31.25 "Cairo"               # Egypt
    22.5    88.3  "Calcutta"            # India
    -33.93   18.47 "Cape Town"           # South Africa
    33.6    -7.6  "Casablanca"          # Morocco (Rabat?)
    41.83  -87.75 "Chicago"             # Illinois, USA
    32.78  -96.80 "Dallas"              # Texas, USA
    28.63   77.20 "New Delhi"           # India
    39.75 -105.00 "Denver"              # Colorado, USA
    24.23   55.28 "Dubai"               # UAE (Abu Dhabi?)
    -27.1  -109.4  "Easter Island"       # Easter Island
    -18.0   178.1  "Fiji"                # Fiji
    13.5   144.8  "Guam"                # Guam
    60.13   25.00 "Helsinki"            # Finland
    22.2   114.1  "Hong Kong"           # Hong Kong
    21.32 -157.83 "Honolulu"            # Hawaii, USA
    52.2   104.3  "Irkutsk"             # Irkutsk, Russia
    41.0    29.0  "Istanbul"            # Turkey (Ankara?)
    -6.13  106.75 "Jakarta"             # Indonesia
    31.8    35.2  "Jerusalem"           # Israel
    34.5    69.2  "Kabul"               # Afghanistan
    27.7    85.3  "Kathmandu"           # Nepal
    50.4    30.5  "Kiev"                # Ukraine
    3.13  101.70 "Kuala Lumpur"        # Malaysia
    6.45    3.47 "Lagos"               # Nigeria
    -12.10  -77.05 "Lima"                # Peru
    51.50   -0.17 "London"              # United Kingdom
    40.42   -3.72 "Madrid"              # Spain
    14.6   121.0  "Manila"              # The Phillipines
    21.5    39.8  "Mecca"               # Saudi Arabia
    19.4   -99.1  "Mexico City"         # Mexico
    25.8   -80.2  "Miami"               # Florida, USA
    6.2   -10.8  "Monrovia"            # Liberia
    45.5   -73.5  "Montreal"            # Quebec, Canada
    55.75   37.70 "Moscow"              # Russia
    -1.28   36.83 "Nairobi"             # Kenya
    59.93   10.75 "Oslo"                # Norway
    48.87    2.33 "Paris"               # France
    -32.0   115.9  "Perth"               # Australia
    45.5  -122.5  "Portland"            # Oregon, USA
    -0.2   -78.5  "Quito"               # Ecuador
    64.15  -21.97 "Reykjavik"           # Iceland
    -22.88  -43.28 "Rio de Janeiro"      # Brazil
    41.88   12.50 "Rome"                # Italy
    11.0   106.7  "Ho Chi Minh City"    # Vietnam (Hanoi?)
    37.75 -122.45 "San Francisco"       # California, USA
    9.98  -84.07 "San Jose"            # Costa Rica
    18.5   -66.1  "San Juan"            # Puerto Rico
    -33.5   -70.7  "Santiago"            # Chile
    1.2   103.9  "Singapore"           # Singapore
    42.67   23.30 "Sofia"               # Bulgaria
    59.33   18.08 "Stockholm"           # Sweden
    -33.92  151.17 "Sydney"              # Australia
    -17.6  -149.5  "Tahiti"              # Tahiti
    16.8    -3.0  "Timbuktu"            # Mali (Bamako?)
    35.67  139.75 "Tokyo"               # Japan
    43.70  -79.42 "Toronto"             # Ontario, Canada
    32.9    13.2  "Tripoli"             # Libya
    47.9   106.9  "Ulan Bator"          # Mongolia
    49.22 -123.10 "Vancouver"           # B.C., Canada
    48.22   16.37 "Vienna"              # Austria
    38.9   -77.0  "Washington"          # United States
    -41.28  174.78 "Wellington"          # New Zealand
    62.5  -114.3  "Yellowknife"         # N.T., Canada
    90.00    0.00 "North Pole"          # North Pole
    -90.00    0.00 "South Pole"          # South Pole
    @enduml

.. end-cities-xearth-diagram-example

This is the code for the example above:

.. literalinclude:: page_more.rst
          :language: rst
          :end-before: end-cities-xearth-diagram-example
          :start-after: begin-cities-xearth-diagram-example

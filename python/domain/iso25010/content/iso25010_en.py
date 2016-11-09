'''
    ISO/IEC 25010 - English

    The quality model is the cornerstone of a product quality evaluation system.
    The quality model determines which quality characteristics will be taken into account
    when evaluating the properties of a software product.

    The quality of a system is the degree to which the system satisfies the stated and implied needs of its various stakeholders,
    and thus provides value. Those stakeholders' needs (functionality, performance, security, maintainability, etc.) are precisely
    what is represented in the quality model, which categorizes the product quality into characteristics and sub-characteristics.
    
    Taken from http://iso25000.com/index.php/en/iso-25000-standards/iso-25010 [ early November 2016 ]
'''
from __future__ import absolute_import
from __future__ import print_function


from ..model import Iso25010MainCharacteristic, Iso25010SubCharacteristic


Iso25010MainCharacteristic(
    "ISO25010.01",
    "Functional Suitability",
    "This characteristic represents the degree to which a product or system provides functions that meet stated and implied needs when used under specified conditions.",

    Iso25010SubCharacteristic(
        "ISO25010.01/01",
        "Functional completeness",
        "Degree to which the set of functions covers all the specified tasks and user objectives.",
    ),

    Iso25010SubCharacteristic(
        "ISO25010.01/02",
        "Functional correctness",
        "Degree to which a product or system provides the correct results with the needed degree of precision.",
    ),

    Iso25010SubCharacteristic(
        "ISO25010.01/02",
        "Functional appropriateness",
        "Degree to which the functions facilitate the accomplishment of specified tasks and objectives.",
    ),

)


Iso25010MainCharacteristic(
    "ISO25010.02",
    "Performance efficiency",
    "This characteristic represents the performance relative to the amount of resources used under stated conditions.",

    Iso25010SubCharacteristic(
        "ISO25010.02/01",
        "Time behaviour",
        "Degree to which the response and processing times and throughput rates of a product or system, when performing its functions, meet requirements.",
    ),

    Iso25010SubCharacteristic(
        "ISO25010.02/02",
        "Resource utilization",
        "Degree to which the amounts and types of resources used by a product or system, when performing its functions, meet requirements.",
    ),

    Iso25010SubCharacteristic(
        "ISO25010.02/03",
        "Capacity",
        "Degree to which the maximum limits of a product or system parameter meet requirements.",
    ),

)


Iso25010MainCharacteristic(
    "ISO25010.03",
    "Compatibility",
    "Degree to which a product, system or component can exchange information with other products, systems or components, and/or perform its required functions, while sharing the same hardware or software environment.",

    Iso25010SubCharacteristic(
        "ISO25010.03/01",
        "Co-existence",
        "Degree to which a product can perform its required functions efficiently while sharing a common environment and resources with other products, without detrimental impact on any other product.",
    ),

    Iso25010SubCharacteristic(
        "ISO25010.03/02",
        "Interoperability",
        "Degree to which two or more systems, products or components can exchange information and use the information that has been exchanged.",
    ),

)


Iso25010MainCharacteristic(
    "ISO25010.04",
    "Usability",
    "Degree to which a product or system can be used by specified users to achieve specified goals with effectiveness, efficiency and satisfaction in a specified context of use.",

    Iso25010SubCharacteristic(
        "ISO25010.04/01",
        "Appropriateness recognizability",
        "Degree to which users can recognize whether a product or system is appropriate for their needs.",
    ),

    Iso25010SubCharacteristic(
        "ISO25010.04/02",
        "Learnability",
        "Degree to which a product or system can be used by specified users to achieve specified goals of learning to use the product or system with effectiveness, efficiency, freedom from risk and satisfaction in a specified context of use.",
    ),

    Iso25010SubCharacteristic(
        "ISO25010.04/03",
        "Operability",
        "Degree to which a product or system has attributes that make it easy to operate and control.",
    ),

    Iso25010SubCharacteristic(
        "ISO25010.04/04",
        "User error protection",
        "Degree to which a system protects users against making errors.",
    ),

    Iso25010SubCharacteristic(
        "ISO25010.04/05",
        "User interface aesthetics",
        "Degree to which a user interface enables pleasing and satisfying interaction for the user.",
    ),

    Iso25010SubCharacteristic(
        "ISO25010.04/06",
        "Accessibility",
        "Degree to which a product or system can be used by people with the widest range of characteristics and capabilities to achieve a specified goal in a specified context of use.",
    ),

)


Iso25010MainCharacteristic(
    "ISO25010.05",
    "Reliability",
    "Degree to which a system, product or component performs specified functions under specified conditions for a specified period of time.",

    Iso25010SubCharacteristic(
        "ISO25010.05/01",
        "Maturity",
        "Degree to which a system, product or component meets needs for reliability under normal operation.",
    ),

    Iso25010SubCharacteristic(
        "ISO25010.05/02",
        "Availability",
        "Degree to which a system, product or component is operational and accessible when required for use.",
    ),

    Iso25010SubCharacteristic(
        "ISO25010.05/03",
        "Fault tolerance",
        "Degree to which a system, product or component operates as intended despite the presence of hardware or software faults.",
    ),

    Iso25010SubCharacteristic(
        "ISO25010.05/04",
        "Recoverability",
        "Degree to which, in the event of an interruption or a failure, a product or system can recover the data directly affected and re-establish the desired state of the system.",
    ),

)


Iso25010MainCharacteristic(
    "ISO25010.06",
    "Security",
    "Degree to which a product or system protects information and data so that persons or other products or systems have the degree of data access appropriate to their types and levels of authorization.",

    Iso25010SubCharacteristic(
        "ISO25010.06/01",
        "Confidentiality",
        "Degree to which a product or system ensures that data are accessible only to those authorized to have access.",
    ),

    Iso25010SubCharacteristic(
        "ISO25010.06/02",
        "Integrity",
        "Degree to which a system, product or component prevents unauthorized access to, or modification of, computer programs or data.",
    ),

    Iso25010SubCharacteristic(
        "ISO25010.06/03",
        "Non-repudiation",
        "Degree to which actions or events can be proven to have taken place, so that the events or actions cannot be repudiated later.",
    ),

    Iso25010SubCharacteristic(
        "ISO25010.06/04",
        "Accountability",
        "Degree to which the actions of an entity can be traced uniquely to the entity.",
    ),

    Iso25010SubCharacteristic(
        "ISO25010.06/05",
        "Authenticity",
        "Degree to which the identity of a subject or resource can be proved to be the one claimed.",
    ),

)


Iso25010MainCharacteristic(
    "ISO25010.07",
    "Maintainability",
    "This characteristic represents the degree of effectiveness and efficiency with which a product or system can be modified to improve it, correct it or adapt it to changes in environment, and in requirements.",

    Iso25010SubCharacteristic(
        "ISO25010.07/01",
        "Modularity",
        "Degree to which a system or computer program is composed of discrete components such that a change to one component has minimal impact on other components.",
    ),

    Iso25010SubCharacteristic(
        "ISO25010.07/02",
        "Reusability",
        "Degree to which an asset can be used in more than one system, or in building other assets.",
    ),

    Iso25010SubCharacteristic(
        "ISO25010.07/03",
        "Analysability",
        "Degree of effectiveness and efficiency with which it is possible to assess the impact on a product or system of an intended change to one or more of its parts, or to diagnose a product for deficiencies or causes of failures, or to identify parts to be modified.",
    ),

    Iso25010SubCharacteristic(
        "ISO25010.07/04",
        "Modifiability",
        "Degree to which a product or system can be effectively and efficiently modified without introducing defects or degrading existing product quality.",
    ),

    Iso25010SubCharacteristic(
        "ISO25010.07/05",
        "Testability",
        "Degree of effectiveness and efficiency with which test criteria can be established for a system, product or component and tests can be performed to determine whether those criteria have been met.",
    ),

)


Iso25010MainCharacteristic(
    "ISO25010.08",
    "Portability",
    "Degree of effectiveness and efficiency with which a system, product or component can be transferred from one hardware, software or other operational or usage environment to another.",

    Iso25010SubCharacteristic(
        "ISO25010.08/01",
        "Adaptability",
        "Degree to which a product or system can effectively and efficiently be adapted for different or evolving hardware, software or other operational or usage environments.",
    ),

    Iso25010SubCharacteristic(
        "ISO25010.08/02",
        "Installability",
        "Degree of effectiveness and efficiency with which a product or system can be successfully installed and/or uninstalled in a specified environment.",
    ),

    Iso25010SubCharacteristic(
        "ISO25010.08/03",
        "Replaceability",
        "Degree to which a product can replace another specified software product for the same purpose in the same environment.",
    ),

)
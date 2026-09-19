# -*- coding: utf-8 -*-
"""
Raw DepEd MATATAG Science CG data, Grades 3-10.
Structure: GRADES[grade] = list of quarters
Each quarter = {
    'q': quarter number (1-4),
    'strand': strand label AS WRITTEN for this grade/quarter (rotates per CG table p.23),
    'cs': [ {'n': cs_number, 'topic': short topic label, 'text': full CS statement} ... ],
    'lc': [ {'n': lc_number, 'text': full LC text, 'cs_n': assigned parent CS number} ... ]
}
Strand codes used for IDs (independent of the rotating label):
MATTER = Materials / Science of Materials
LIVING = Living Things / Life Science
FORCE  = Force, Motion, and Energy
EARTH  = Earth and Space / Earth and Space Science
"""

STRAND_CODE = {
    "Materials": "MATTER",
    "Science of Materials": "MATTER",
    "Living Things": "LIVING",
    "Life Science": "LIVING",
    "Force, Motion, and Energy": "FORCE",
    "Earth and Space": "EARTH",
    "Earth and Space Science": "EARTH",
}

GRADES = {}

# ============================================================= GRADE 3
GRADES[3] = [
    {
        "q": 1, "strand": "Materials",
        "cs": [
            {"n": 1, "topic": "Science in our daily life", "text": "Science is important in understanding how the natural world works."},
            {"n": 2, "topic": "Science processes", "text": "Using science process skills, simple science equipment, and participating in guided activities leads to better understanding of science."},
            {"n": 3, "topic": "Materials and their uses", "text": "Physical properties of materials determine their use."},
        ],
        "lc": [
            {"n": 1, "text": "identify objects, activities, or natural events observed in their local environment that can be explained by science", "cs_n": 1},
            {"n": 2, "text": "participate in guided science activities by asking questions and tinkering with materials", "cs_n": 2},
            {"n": 3, "text": "describe the uses of various science equipment and materials used in simple activities, such as a ruler, hand lens, scissors, balloons, modeling clay, and cardboard", "cs_n": 2},
            {"n": 4, "text": "describe different science process skills used in performing simple science activities, such as observing, predicting, and measuring using units such as millimeter, centimeter, and meter", "cs_n": 2},
            {"n": 5, "text": "describe the physical properties of solid materials, such as hard, shiny, or stretchable", "cs_n": 3},
            {"n": 6, "text": "explain that changes in materials can be harmful to living and non-living things in the environment, such as trash disposal, and burning household materials", "cs_n": 3},
            {"n": 7, "text": "demonstrate proper handling and disposal of materials according to their properties, such as reusing objects, disposing of excess oil into garbage, and recycling paper, plastic or glass", "cs_n": 3},
            {"n": 8, "text": "describe how changes in solid materials make them useful, such as when they are shaped, pressed, hammered, joined, or cut", "cs_n": 3},
            {"n": 9, "text": "identify the properties and uses of metals used by the local community such as iron, gold, silver, and copper", "cs_n": 3},
        ],
    },
    {
        "q": 2, "strand": "Living Things",
        "cs": [
            {"n": 1, "topic": "Guided science activities using process skills", "text": "Using science process skills, simple pieces of science equipment, and participating in guided activities leads to a better understanding of science."},
            {"n": 2, "topic": "Living and nonliving things", "text": "Characteristics of growth, response and reproduction identify living things."},
            {"n": 3, "topic": "Characteristics of living things", "text": "Body parts of plants and animals enable them to live and grow."},
            {"n": 4, "topic": "Basic needs of living things", "text": "All living things have the same basic needs that need to be met by their environment."},
        ],
        "lc": [
            {"n": 1, "text": "use the skills of observing, predicting, and measuring in performing simple guided science activities", "cs_n": 1},
            {"n": 2, "text": "observe and describe the difference between living and non-living things and give examples of each that can be found in the local environment", "cs_n": 2},
            {"n": 3, "text": "describe the characteristics of living things: they grow, respond, and reproduce", "cs_n": 2},
            {"n": 4, "text": "observe and describe the outer body parts of animals, such as head, legs or wings, and identify their role to move and to gather food", "cs_n": 3},
            {"n": 5, "text": "observe the outer parts of plants, such as leaves, roots, and stems and identify their role to get water and nutrients from the soil", "cs_n": 3},
            {"n": 6, "text": "identify the basic needs of all living things, such as air, food, water, and shelter", "cs_n": 4},
            {"n": 7, "text": "observe examples and explain how living things depend on one another and on the environment to meet their basic needs", "cs_n": 4},
            {"n": 8, "text": "recognize that there is a need to protect and conserve the environment for living things to survive", "cs_n": 4},
        ],
    },
    {
        "q": 3, "strand": "Force, Motion, and Energy",
        "cs": [
            {"n": 1, "topic": "Exploring and Questioning", "text": "Objects that change position encounter a push or a pull."},
            {"n": 2, "topic": "Moving objects", "text": "Using science processes and curiosity is important in understanding how objects move."},
            {"n": 3, "topic": "Light and sound", "text": "Light and sound are examples of energy that affect daily life. People can modify light and sound to make them useful."},
        ],
        "lc": [
            {"n": 1, "text": "explore and demonstrate different ways to make objects move by natural causes, such as wind and water, or by people, such as pushing, pulling, rolling, and carrying", "cs_n": 1},
            {"n": 2, "text": "explore and describe things that affect the movement of objects, including size, shape, heaviness, material, and surface texture", "cs_n": 2},
            {"n": 3, "text": "measure and describe changes in the position of people or objects in relation to their original position, such as moving closer, farther, left, or right", "cs_n": 2},
            {"n": 4, "text": "explore and describe how sound is made and transferred in everyday situations, such as the ringing of a bell or the hearing of noises", "cs_n": 3},
            {"n": 5, "text": "describe sources of light and their use in everyday situations", "cs_n": 3},
            {"n": 6, "text": "participate in guided science activities to explore and describe sources of light, how it behaves or can be changed, and its uses in everyday situations", "cs_n": 3},
            {"n": 7, "text": "explain how light and sound can be harmful to people and make suggestions on how to protect oneself from them", "cs_n": 3},
            {"n": 8, "text": "participate in guided activities to explore and describe some ways to use movement, sound, and light to send information between two people", "cs_n": 3},
        ],
    },
    {
        "q": 4, "strand": "Earth and Space",
        "cs": [
            {"n": 1, "topic": "The Non-Living environment", "text": "Non-living things found in the environment are the sources of useful products."},
            {"n": 2, "topic": "Patterns in the weather", "text": "Weather affects our daily activities and may pose threats to health and safety."},
            {"n": 3, "topic": "Celestial objects", "text": "The natural objects in the sky affect the activities of people."},
        ],
        "lc": [
            {"n": 1, "text": "participate in guided activities to locate and describe different types of non-living things found in and around their school, such as rocks, soil, water, air, metals, clouds, rain, and sunlight", "cs_n": 1},
            {"n": 2, "text": "identify some useful things that people have made from non-living materials and describe what natural materials have been used to make the items", "cs_n": 1},
            {"n": 3, "text": "recognize that the non-living materials that make up the environment are referred to as 'earth materials'", "cs_n": 1},
            {"n": 4, "text": "observe and record changes in the weather during a day or over some days and describe the different types and patterns of weather that occur in the local area", "cs_n": 2},
            {"n": 5, "text": "describe how changes in the weather can affect daily activities and explain how some types of weather can be dangerous for people", "cs_n": 2},
            {"n": 6, "text": "participate in guided activities to carefully observe and describe the natural objects commonly seen in the sky during daytime and nighttime, including the Sun, the Moon, planets, and stars", "cs_n": 3},
            {"n": 7, "text": "participate in guided activities to explore and record how and when the Sun, the Moon, planets, and stars can be seen moving across the sky", "cs_n": 3},
            {"n": 8, "text": "explain how natural objects in the sky affect activities of people", "cs_n": 3},
            {"n": 9, "text": "describe safety measures that people can use to avoid the harmful effects of the Sun's light", "cs_n": 3},
        ],
    },
]

# ============================================================= GRADE 4
GRADES[4] = [
    {
        "q": 1, "strand": "Materials",
        "cs": [
            {"n": 1, "topic": "Science inventions", "text": "Science inventions have brought about major changes to our daily lives."},
            {"n": 2, "topic": "Materials and their uses", "text": "Chemical properties of materials determine their uses."},
            {"n": 3, "topic": "Gathering scientific information", "text": "Communication skills and open mindedness are needed in solving environmental issues."},
        ],
        "lc": [
            {"n": 1, "text": "use information from secondary sources to identify a famous Filipino and/or foreign scientist and their invention/s", "cs_n": 1},
            {"n": 2, "text": "use information from the home or the local community to identify a science invention and explain its impact on their everyday life", "cs_n": 1},
            {"n": 3, "text": "describe the chemical properties of materials, such as they can be burnt, react with other materials, or are degradable or biodegradable", "cs_n": 2},
            {"n": 4, "text": "describe changes in properties of materials when exposed to certain changes in temperature, such as changes when wood or coal are burned", "cs_n": 2},
            {"n": 5, "text": "demonstrate ways to minimize harmful changes in materials, such as restriction of burning of waste materials, and care in handling reactive materials", "cs_n": 2},
            {"n": 6, "text": "identify issues and concerns in the local community and how they could be addressed by science, such as the treatment of waste", "cs_n": 3},
            {"n": 7, "text": "apply science process skills and attitudes in conducting a guided survey about environmental issues and concerns including grouping and classifying, communicating, and open mindedness", "cs_n": 3},
        ],
    },
    {
        "q": 2, "strand": "Living Things",
        "cs": [
            {"n": 1, "topic": "Systems in plants and animals", "text": "Animals and plants have systems that function to keep them alive."},
            {"n": 2, "topic": "Plants and animals and their habitats", "text": "Animals and plants live in habitats that meet their basic needs."},
            {"n": 3, "topic": "Life cycles of animals", "text": "Animals have life cycles that include development and reproduction."},
            {"n": 4, "topic": "Animals and the food they eat", "text": "Animals can be grouped according to the food that they eat."},
            {"n": 5, "topic": "Food chains", "text": "Food chains show a series of living things that depend on each other for food. Using drawings, tables, and flowcharts is an important skill in learning science concepts and in learning about science processes."},
        ],
        "lc": [
            {"n": 1, "text": "describe in simple terms how the following human body systems work: muscular, skeletal, digestive, circulatory, and respiratory", "cs_n": 1},
            {"n": 2, "text": "observe the root and shoot system in plants and describe why they are important", "cs_n": 1},
            {"n": 3, "text": "use a drawing or diagram to classify some Philippine animals and plants, based on their habitat: some live on land (terrestrial), live in water (aquatic) or fly in the air (aerial)", "cs_n": 2},
            {"n": 4, "text": "make a list or draw up a table with examples of animals and plants in a particular habitat, such as a garden, rice field, seashore, and mangrove swamp", "cs_n": 2},
            {"n": 5, "text": "use flow charts to compare the different stages in the life cycle of animals, such as a butterfly, frog, chicken, and human", "cs_n": 3},
            {"n": 6, "text": "use information from secondary sources to group animals according to the food they eat: plant eaters (herbivores), meat eaters (carnivores), and plant and meat-eaters (omnivores)", "cs_n": 4},
            {"n": 7, "text": "draw a simple food chain using living things from the Philippines and label them as herbivores, carnivores, and omnivores", "cs_n": 5},
        ],
    },
    {
        "q": 3, "strand": "Force, Motion, and Energy",
        "cs": [
            {"n": 1, "topic": "Forces and movement", "text": "Science processes help in observing and predicting how things move. Pushes and pulls can change the position and shape of objects."},
            {"n": 2, "topic": "Observing, measuring, and predicting", "text": "Gathering scientific information helps explain the behavior of objects and materials."},
            {"n": 3, "topic": "Magnets", "text": "Magnets affect some objects and materials without touching them."},
            {"n": 4, "topic": "Sound, light, and heat energy", "text": "Energy is present whenever there is movement, sound, light, or heat."},
        ],
        "lc": [
            {"n": 1, "text": "participate in guided activities to discover and predict how rigid and soft objects can be moved and/or changed in shape", "cs_n": 1},
            {"n": 2, "text": "measure accurately the distance and time when things move using simple equipment", "cs_n": 2},
            {"n": 3, "text": "identify that how far an object moves in a given time is called speed", "cs_n": 2},
            {"n": 4, "text": "construct and label simple graphs of different speeds including stationary and uniform speeds, both fast and slow", "cs_n": 2},
            {"n": 5, "text": "participate in guided activities to demonstrate that pushes and pulls can be used to change the speed and direction of an object including making it go faster, turn it to a different direction, slow it down, and stop it", "cs_n": 1},
            {"n": 6, "text": "demonstrate through guided activities that pushes and pulls can be used to change the speed and direction of an object", "cs_n": 1},
            {"n": 7, "text": "determine how forces can change the shape of objects such as when they are pushed, pulled, stretched, bent, twisted, or squeezed", "cs_n": 1},
            {"n": 8, "text": "carry out guided investigations to identify the properties of magnets, including how they affect other magnets and objects made of different materials", "cs_n": 3},
            {"n": 9, "text": "identify examples of how objects can affect other objects even when they are not in contact with each other, such as magnets attracting other objects, light from the sun affecting our eyes and skin, and loud noises hurting our ears", "cs_n": 3},
            {"n": 10, "text": "identify that energy is something that can cause change including light, sound, and heat energy", "cs_n": 4},
            {"n": 11, "text": "observe and identify sources and uses of light, sound, and heat energy at school, at home and in the local community", "cs_n": 4},
        ],
    },
    {
        "q": 4, "strand": "Earth and Space",
        "cs": [
            {"n": 1, "topic": "Soils", "text": "Soil and water resources are needed by plants and animals to live and grow."},
            {"n": 2, "topic": "Characteristics of weather", "text": "Characteristics of the weather can be observed and measured."},
            {"n": 3, "topic": "Characteristics of the Sun", "text": "The Sun is a ball of hot gases about 100 times the size of Earth, which radiates light energy needed by living things."},
        ],
        "lc": [
            {"n": 1, "text": "participate in guided activities using simple equipment to compare different types of soil including sandy, clay, silt, and loam, including comparing the ability of the soils to hold water", "cs_n": 1},
            {"n": 2, "text": "recognize that water is one of the basic needs of plants and animals", "cs_n": 1},
            {"n": 3, "text": "participate in a guided investigation to identify the effect of different types of soil on the growth of plants", "cs_n": 1},
            {"n": 4, "text": "identify some of the basic characteristics used to describe the weather, such as air temperature, air pressure, wind speed, wind direction, humidity, rain, and cloud cover", "cs_n": 2},
            {"n": 5, "text": "use weather instruments to measure and record some of the characteristics of weather during a school day", "cs_n": 2},
            {"n": 6, "text": "examine a local weather chart to make simple interpretations about the local weather and how it might change and describe and practice safety precautions to use during poor or extreme weather conditions", "cs_n": 2},
            {"n": 7, "text": "describe some of the overall characteristics of the Sun, such as its composition, its size, and the main energy it radiates", "cs_n": 3},
            {"n": 8, "text": "describe the changes in the direction and length of shadows from a shadow stick and use the information to infer why the Sun changes position during a day", "cs_n": 3},
            {"n": 9, "text": "make suggestions about the importance of the Sun to living things for a group or class discussion and confirm and record ideas by referring to trustworthy secondary sources of information", "cs_n": 3},
        ],
    },
]

# ============================================================= GRADE 5
GRADES[5] = [
    {
        "q": 1, "strand": "Materials",
        "cs": [
            {"n": 1, "topic": "Matter in daily life", "text": "Scientists identify three states of matter based on shape and volume."},
            {"n": 2, "topic": "Matter and the three states", "text": "Temperature can cause changes of state."},
            {"n": 3, "topic": "Scientific investigation", "text": "Planned simple scientific investigations require several steps and processes. An understanding of matter can be applied to solve real world problems."},
        ],
        "lc": [
            {"n": 1, "text": "describe matter as anything that has mass and takes up space", "cs_n": 1},
            {"n": 2, "text": "identify that matter has (exists in) three states called solids, liquids, and gases", "cs_n": 1},
            {"n": 3, "text": "describe the properties of solids, liquids, and gases in terms of shape and volume: solids (definite shape and volume), liquids (no definite shape; definite volume), gases (no definite shape or volume)", "cs_n": 1},
            {"n": 4, "text": "identify objects at home and in the classroom as solid, liquid or gas", "cs_n": 1},
            {"n": 5, "text": "use measuring cylinders or beakers to measure volume using units, such as milliliters (mL), and liters (L)", "cs_n": 3},
            {"n": 6, "text": "describe how changes in temperature cause matter to change in state, such as solid to liquid to gas", "cs_n": 2},
            {"n": 7, "text": "describe the steps of a simple science investigation: What is the problem? What materials do you need? What do you need to do? What have you found out/learned?", "cs_n": 3},
            {"n": 8, "text": "identify and appropriately use units in simple science activities, such as milligrams (mg), grams (g), kilograms (kg), and degrees centigrade (\u00b0C)", "cs_n": 3},
            {"n": 9, "text": "plan simple scientific investigations in answering questions, such as \u201cDo gases (like air) or liquids (like water) have mass?\u201d, using appropriate simple science equipment, such as a balance, and a thermometer, with appropriate units", "cs_n": 3},
        ],
    },
    {
        "q": 2, "strand": "Living Things",
        "cs": [
            {"n": 1, "topic": "Body systems in animals", "text": "Animals have systems that help them grow, respond, and reproduce."},
            {"n": 2, "topic": "Plants, animals, and microorganisms", "text": "Living things can be grouped as plants, animals, and microorganisms based on their characteristics."},
            {"n": 3, "topic": "Life cycles of living things", "text": "The life cycles of plants and animals allow them to survive and reproduce."},
            {"n": 4, "topic": "Specialized structures in plants", "text": "Plants have specialized structures that help them overcome unfavorable conditions."},
        ],
        "lc": [
            {"n": 1, "text": "identify from pictures and labeled diagrams the parts of the digestive system as mouth, gullet, stomach, small intestine, and large intestine, and describe how they work", "cs_n": 1},
            {"n": 2, "text": "identify from pictures and diagrams the parts of the respiratory system as the nose, windpipe, and lungs, and describe how they work", "cs_n": 1},
            {"n": 3, "text": "identify from pictures and labeled diagrams the parts of the female reproductive system as ovaries, uterus, and vagina and those of the male reproductive system as the prostate, testis, and penis and describe how they work", "cs_n": 1},
            {"n": 4, "text": "use a table to show how living things can be classified into groups based on similar characteristics: plants (flowering and non-flowering); animals (mammals, reptiles, insects, birds, fish, amphibians); microorganisms (fungi and bacteria)", "cs_n": 2},
            {"n": 5, "text": "identify which groups of animals reproduce by giving birth to live young, such as mammals, and which reproduce by laying eggs, such as birds and reptiles", "cs_n": 2},
            {"n": 6, "text": "compare the life cycles of mammals from birth to adulthood, birds from egg to a mature organism, and plants from seed to a young plant, and then to a mature plant", "cs_n": 3},
            {"n": 7, "text": "describe the purpose of specialized structures in plants, such as rhizomes, tubers, thorns, bulbs, and aerial roots", "cs_n": 4},
            {"n": 8, "text": "explain how some plants have adapted to unfavorable conditions in the environment, such as lack of rain or floods", "cs_n": 4},
            {"n": 9, "text": "use information from secondary sources to describe examples of how some animals have changed to better suit their environment, such as mimicry or camouflage", "cs_n": 4},
        ],
    },
    {
        "q": 3, "strand": "Force, Motion, and Energy",
        "cs": [
            {"n": 1, "topic": "Contact and non-contact forces", "text": "Science investigations provide evidence to support predictions and explanations. Forces are pushes or pulls that act in a specific direction."},
            {"n": 2, "topic": "Investigating scientifically / Friction", "text": "Friction is an everyday force created by two surfaces interacting."},
            {"n": 3, "topic": "Gravity", "text": "Gravity causes all objects to fall towards the ground."},
            {"n": 4, "topic": "Static electricity", "text": "Static electricity occurs when some materials rub on other materials causing charges to jump."},
            {"n": 5, "topic": "Conductors, insulators, and simple circuits", "text": "Electric current requires a pathway for charges to flow."},
        ],
        "lc": [
            {"n": 1, "text": "carry out simple investigations to demonstrate that contact forces cause objects to move in the same direction as the direction that the force is applied", "cs_n": 1},
            {"n": 2, "text": "plan and carry out a scientific investigation to determine the effect of different surfaces on the size of frictional forces", "cs_n": 2},
            {"n": 3, "text": "demonstrate how friction can produce heat and investigate ways of reducing and increasing friction", "cs_n": 2},
            {"n": 4, "text": "identify gravity as a non-contact force that affects the behaviors of materials and objects on Earth in predictable ways", "cs_n": 3},
            {"n": 5, "text": "predict and explain whether heavier objects will fall faster than lighter objects due to the force of gravity", "cs_n": 3},
            {"n": 6, "text": "observe and describe the effects of gravity to the motion of an object", "cs_n": 3},
            {"n": 7, "text": "investigate the effects of static electricity using common materials, such as a comb, plastic and glass rods, and balloons", "cs_n": 4},
            {"n": 8, "text": "assemble and draw a simple circuit using batteries, wires, switch, and bulb and/or toy motor or buzzer", "cs_n": 5},
            {"n": 9, "text": "design and construct a simple electrical circuit to identify what materials will conduct electricity and use it to identify materials from the environment that will and will not conduct electricity", "cs_n": 5},
            {"n": 10, "text": "make a simple electromagnet and observe and record its properties", "cs_n": 5},
        ],
    },
    {
        "q": 4, "strand": "Earth and Space",
        "cs": [
            {"n": 1, "topic": "Landforms, rocks and minerals", "text": "Landforms influence living and non-living components of the environment."},
            {"n": 2, "topic": "Weathering and erosion (using models)", "text": "Rocks are composed of grains of minerals that break down to form soil. Weathering and erosion shape the Earth's surface by breaking down and transporting rocks."},
            {"n": 3, "topic": "The Water Cycle", "text": "The Water Cycle includes processes of evaporation, precipitation and transportation."},
            {"n": 4, "topic": "Weather disturbances", "text": "Weather disturbances feature low pressure, strong winds, and storms."},
            {"n": 5, "topic": "The Solar System", "text": "The planets and moons vary in physical features and composition. Phases of the Moon depend on its position relative to Earth and Sun."},
        ],
        "lc": [
            {"n": 1, "text": "identify local examples of natural landforms and bodies of water such as mountains, valleys, rivers, and coastlines, and describe how they influence non-living and living components of the environment", "cs_n": 1},
            {"n": 2, "text": "explore the school grounds or the local area to observe or collect different types of rocks, describing their similarities or differences in terms of their features, such as texture, color, and grain crystal size", "cs_n": 2},
            {"n": 3, "text": "classify common rocks from provided samples using a simple rock classification system, such as a dichotomous key", "cs_n": 2},
            {"n": 4, "text": "explain how soil is formed from rocks and minerals", "cs_n": 2},
            {"n": 5, "text": "demonstrate how erosion transports Earth materials", "cs_n": 2},
            {"n": 6, "text": "explain the role of the water cycle in the environment", "cs_n": 3},
            {"n": 7, "text": "construct a model to communicate some of the key processes in the water cycle", "cs_n": 3},
            {"n": 8, "text": "describe some effects of weather disturbances that occur in or near the Philippines", "cs_n": 4},
            {"n": 9, "text": "describe the weather conditions according to a Public Storm Warning Signal issued by the Philippines Atmospheric, Geological and Astronomical Services Administration (PAGASA)", "cs_n": 4},
            {"n": 10, "text": "describe typical weather conditions before, during and after a tropical cyclone", "cs_n": 4},
            {"n": 11, "text": "describe the general structure of the solar system, identifying the names of the major celestial objects, their main features, and general composition", "cs_n": 5},
            {"n": 12, "text": "make drawings or a simple model to show the motion of the Earth and Moon relative to the Sun to explain the phases of the moon that people see from Earth", "cs_n": 5},
        ],
    },
]

# ============================================================= GRADE 6
GRADES[6] = [
    {
        "q": 1, "strand": "Materials",
        "cs": [
            {"n": 1, "topic": "Diagrams and flowcharts", "text": "Diagrams and flowcharts demonstrate processes involving heat energy and changes of state."},
            {"n": 2, "topic": "Processes of changes of state", "text": "Changes in materials can be either reversible or irreversible."},
            {"n": 3, "topic": "Physical and chemical change / Mixtures and separation techniques", "text": "Mixtures and the products of their separation techniques are very useful in our daily lives."},
            {"n": 4, "topic": "Scientific investigation (fair test)", "text": "Scientific investigations need to satisfy the features of a fair test and use accurate and reliable measurements."},
        ],
        "lc": [
            {"n": 1, "text": "describe changes of state for solids, liquids, and gases as melting, evaporation, freezing, condensation using diagrams and flowcharts", "cs_n": 1},
            {"n": 2, "text": "explain the role of heat energy in change of state processes", "cs_n": 1},
            {"n": 3, "text": "explain why physical changes are reversible, and chemical changes are irreversible", "cs_n": 2},
            {"n": 4, "text": "describe useful everyday examples of uniform and non-uniform mixtures, such as solutions and suspensions", "cs_n": 3},
            {"n": 5, "text": "describe air as a mixture of oxygen, carbon dioxide, nitrogen, and water vapor", "cs_n": 3},
            {"n": 6, "text": "demonstrate various techniques in separating mixtures, such as decantation, winnowing, scooping, picking, evaporation, filtering, sieving, and using magnets", "cs_n": 3},
            {"n": 7, "text": "explain the benefits of each mixture separation technique in preparing useful products", "cs_n": 3},
            {"n": 8, "text": "apply the features of a fair test: change one factor, measure one factor, and keep all other factors the same", "cs_n": 4},
            {"n": 9, "text": "recognize the features of a fair test and that scientific investigations also involve doing at least three trials (replication), and observing, measuring, and recording accurately", "cs_n": 4},
        ],
    },
    {
        "q": 2, "strand": "Living Things",
        "cs": [
            {"n": 1, "topic": "The circulatory system", "text": "Animals have systems that help them grow, respond, and reproduce."},
            {"n": 2, "topic": "Reproduction in plants", "text": "There are several modes of reproduction in plants."},
            {"n": 3, "topic": "Vertebrates and invertebrates", "text": "To be valid and reliable, scientific investigations need to include fair tests and multiple trials. Animals can be grouped as vertebrates or invertebrates based on their characteristics."},
            {"n": 4, "topic": "Food webs", "text": "Producers, consumers, scavengers, and decomposers have important roles in food webs."},
            {"n": 5, "topic": "Interactions between living things / Biotic and abiotic factors", "text": "Interactions within an ecosystem can have important impacts on the living things within it."},
        ],
        "lc": [
            {"n": 1, "text": "identify from pictures and diagrams the parts of the circulatory system as heart, blood, and blood vessels, and describe how they work", "cs_n": 1},
            {"n": 2, "text": "describe the different ways that plants reproduce, such as pollination, seed production, and plant propagation", "cs_n": 2},
            {"n": 3, "text": "plan a simple scientific investigation that includes the features of a fair test, replication, and accurate measurement to determine which type of plant propagation, such as cutting, budding, layering, grafting, works best for garden plants", "cs_n": 2},
            {"n": 4, "text": "describe the differences between animals with a backbone (vertebrates) and animals without backbones (invertebrates) by using common local examples of each group", "cs_n": 3},
            {"n": 5, "text": "describe the roles of producers, consumers, scavengers, and decomposers in a food web", "cs_n": 4},
            {"n": 6, "text": "use information from secondary sources to describe that living things interact with each other in the natural environment, such as through competition, or predation", "cs_n": 5},
            {"n": 7, "text": "describe living things, such as animals and plants, as biotic factors and light, water, temperature, and soil type, as abiotic factors of an ecosystem", "cs_n": 5},
            {"n": 8, "text": "explain how interaction between living things and interactions between living and non-living things may bring good or harm to the living things involved", "cs_n": 5},
        ],
    },
    {
        "q": 3, "strand": "Force, Motion, and Energy",
        "cs": [
            {"n": 1, "topic": "Simple machines", "text": "Simple machines allow people to change the direction and size of forces."},
            {"n": 2, "topic": "Properties of water and sound waves", "text": "Waves transfer energy between source and receiver."},
            {"n": 3, "topic": "Longitudinal and Transverse waves", "text": "Science processes and concepts help solve everyday problems."},
        ],
        "lc": [
            {"n": 1, "text": "observe and describe examples and uses of simple machines found at home, at school, and in the community", "cs_n": 1},
            {"n": 2, "text": "demonstrate through guided investigation the advantages and limitations of simple machines such as inclined planes, wedges, levers, and pulleys", "cs_n": 1},
            {"n": 3, "text": "carry out fair tests to show how levers can be used to change the magnitude and direction of a force", "cs_n": 1},
            {"n": 4, "text": "identify that waves carry energy from a source to a receiver", "cs_n": 2},
            {"n": 5, "text": "carry out investigations with water waves in a ripple tank, a big tub of water or improvised ripple tank and observe and describe the features of the waves including their shape (crests and troughs), size (width and height), and patterns of movement (how they bend, or reflect off walls)", "cs_n": 2},
            {"n": 6, "text": "research using secondary sources to identify how the properties of waves are described using scientific terms such as amplitude, frequency, wavelength, and velocity", "cs_n": 2},
            {"n": 7, "text": "identify differences and similarities between longitudinal waves and transverse waves", "cs_n": 3},
            {"n": 8, "text": "demonstrate using simple models how longitudinal waves and transverse waves carry energy", "cs_n": 3},
            {"n": 9, "text": "identify some examples of longitudinal waves, and transverse waves", "cs_n": 3},
            {"n": 10, "text": "describe and explain how sound changes when the source or the receiver are moving", "cs_n": 3},
        ],
    },
    {
        "q": 4, "strand": "Earth and Space",
        "cs": [
            {"n": 1, "topic": "Volcanic activity and safety", "text": "Volcanoes are vents from which molten rock from Earth's crust erupts onto the surface releasing pressure and gases. The Philippine volcanoes can violently and unpredictably erupt lava, ash, and ballistic projectiles."},
            {"n": 2, "topic": "Seasons in the Philippines", "text": "Weather and climate have predictable patterns throughout the year, which affect human activities."},
            {"n": 3, "topic": "Motions of the Earth", "text": "The revolution and the rotation of the Earth demonstrate observable patterns."},
            {"n": 4, "topic": "Constellations", "text": "Constellations are patterns of stars in the sky."},
        ],
        "lc": [
            {"n": 1, "text": "explain what volcanoes are and how they are formed", "cs_n": 1},
            {"n": 2, "text": "use local information or other reliable sources to identify where the nearest active and inactive volcanoes are located and assess the risk of impacts from eruptions to their local community", "cs_n": 1},
            {"n": 3, "text": "discuss the patterns of volcanic eruptions in the Philippines over the last 100 years with family and community members to assess and describe how predictable patterns of eruptions are", "cs_n": 1},
            {"n": 4, "text": "identify and describe some of the materials formed during volcanic eruptions in the Philippines", "cs_n": 1},
            {"n": 5, "text": "interpret PHIVOLCS Volcano Monitoring (Alert Levels) to demonstrate what to do before, during, and after a volcanic eruption", "cs_n": 1},
            {"n": 6, "text": "describe the different seasons in the Philippines and suggest activities that are appropriate for each season", "cs_n": 2},
            {"n": 7, "text": "demonstrate the rotation of the Earth on its axis using a globe to explain day and night", "cs_n": 3},
            {"n": 8, "text": "make a Sun-Earth-Moon system model to demonstrate and explain the observable effects of predictable patterns and events including changes in seasons, changes observed in the patterns of visible stars over a year, and solar and lunar eclipses", "cs_n": 3},
            {"n": 9, "text": "explain why ancient human cultures relied on constellations to indicate directions and verify seasons", "cs_n": 4},
            {"n": 10, "text": "gather information from local indigenous community members or from reliable secondary sources to investigate ways that indigenous people of the Philippines represented and communicated understandings of the predictability of solar and lunar eclipses, and patterns/interpretations in the night sky and their use for tracking time", "cs_n": 4},
        ],
    },
]

# ============================================================= GRADE 7
GRADES[7] = [
    {
        "q": 1, "strand": "Science of Materials",
        "cs": [
            {"n": 1, "topic": "Use of models", "text": "Scientists use models to explain phenomena."},
            {"n": 2, "topic": "The Particle model and changes of state", "text": "The particle model explains the properties of solids, liquids, and gases and the processes involved in changes of state. Diagrams and flowcharts are very useful in demonstrating and explaining the motion and arrangement of particles during changes of state."},
            {"n": 3, "topic": "Planning, following, and recording scientific investigations", "text": "There are specific processes for planning, conducting, and recording scientific investigations."},
            {"n": 4, "topic": "Solutions, solubility, and concentration", "text": "The properties of solutions such as solubility and reaction to litmus determine their use."},
        ],
        "lc": [
            {"n": 1, "text": "recognize that scientists use models to explain phenomena that cannot be easily seen or detected", "cs_n": 1},
            {"n": 2, "text": "describe the Particle Model of Matter as \u201cAll matter is made up of tiny particles with each pure substance having its own kind of particles.\u201d", "cs_n": 2},
            {"n": 3, "text": "describe that particles are constantly in motion, have spaces between them, attract each other, and move faster as the temperature increases (or with the addition of heat)", "cs_n": 2},
            {"n": 4, "text": "use diagrams and illustrations to describe the arrangement, spacing, and relative motion of the particles in each of the three states (phases) of matter", "cs_n": 2},
            {"n": 5, "text": "explain the changes of state in terms of particle arrangement and energy changes: solid to liquid to vapor, and vapor to liquid to solid", "cs_n": 2},
            {"n": 6, "text": "follow appropriate steps of a scientific investigation which includes: aim/problem, materials and equipment, method/procedures, results including data, and conclusion", "cs_n": 3},
            {"n": 7, "text": "make accurate measurements using standard units for physical quantities and organize the collected data when carrying out a scientific investigation", "cs_n": 3},
            {"n": 8, "text": "identify the role of the solute and solvent in a solution", "cs_n": 4},
            {"n": 9, "text": "express quantitatively the amount of solute present in a given volume of solvent", "cs_n": 4},
            {"n": 10, "text": "demonstrate how different factors affect the solubility of a solute in a given solvent, such as heat", "cs_n": 4},
            {"n": 11, "text": "identify solutions, which can be found at home and in school and that react with litmus indicator, as acids, bases, and salts", "cs_n": 4},
            {"n": 12, "text": "demonstrate proper use and handling of science equipment", "cs_n": 3},
        ],
    },
    {
        "q": 2, "strand": "Life Science",
        "cs": [
            {"n": 1, "topic": "Science equipment: the compound microscope", "text": "Familiarity and proper use of a compound microscope are essential to observe cells."},
            {"n": 2, "topic": "Plant and animal cells", "text": "The organelles of plant and animal cells can be identified using a compound microscope."},
            {"n": 3, "topic": "Cellular reproduction", "text": "Cells are the basic unit of life and mitosis, and meiosis are the basic forms of cell division. Fertilization occurs when a male reproductive cell fuses with a female reproductive cell. Sexual reproduction is the basis of heredity."},
            {"n": 4, "topic": "Levels of biological organization", "text": "The level of biological organization provides a simple way of connecting the simplest part of the living world to the most complex."},
            {"n": 5, "topic": "Trophic levels and the transfer of energy", "text": "Identifying trophic levels helps understand the transfer of energy from one organism to another as shown in a food pyramid."},
        ],
        "lc": [
            {"n": 1, "text": "identify the parts and functions, and demonstrate proper handling and storing of a compound microscope", "cs_n": 1},
            {"n": 2, "text": "use proper techniques in observing and identifying the parts of a cell with a microscope such as the cell membrane, nucleus, cytoplasm, mitochondria, chloroplasts, and ribosomes", "cs_n": 2},
            {"n": 3, "text": "recognize that some organisms consist of a single cell (unicellular) like in bacteria and some consist of many cells (multicellular) like in a human", "cs_n": 2},
            {"n": 4, "text": "differentiate plant and animal cells based on their organelles", "cs_n": 2},
            {"n": 5, "text": "recognize that cells reproduce through two types of cell division, mitosis and meiosis, and describe mitosis as cell division for growth and repair", "cs_n": 3},
            {"n": 6, "text": "explain that genetic information is passed on to offspring from both parents by the process of meiosis and fertilization", "cs_n": 3},
            {"n": 7, "text": "differentiate sexual from asexual reproduction in terms of number of parents involved, and similarities of offspring to parents", "cs_n": 3},
            {"n": 8, "text": "use a labelled diagram to describe the connections between the levels of biological organization to one another from cells to the biosphere", "cs_n": 4},
            {"n": 9, "text": "describe the trophic levels of an organism as levels of energy in a food pyramid", "cs_n": 5},
            {"n": 10, "text": "use examples of food pyramids to describe the transfer of energy between organisms from one trophic level to another", "cs_n": 5},
        ],
    },
    {
        "q": 3, "strand": "Force, Motion, and Energy",
        "cs": [
            {"n": 1, "topic": "Balanced and unbalanced forces", "text": "Scientists and engineers analyze forces to predict their effects on movement."},
            {"n": 2, "topic": "Motion: displacement and velocity", "text": "Vectors differentiate the concepts of speed and velocity."},
            {"n": 3, "topic": "Distance-Time graphs", "text": "Graphing motion provides more accurate predictions about speed and velocity."},
            {"n": 4, "topic": "Identifying and controlling variables", "text": "The particle model explains natural systems and processes."},
            {"n": 5, "topic": "Heat transfer", "text": "Scientists and engineers conduct innovative research to find solutions to the current global energy crisis by seeking renewable energy solutions."},
        ],
        "lc": [
            {"n": 1, "text": "identify that forces act between objects and can be measured", "cs_n": 1},
            {"n": 2, "text": "identify and describe everyday situations that demonstrate balanced forces (such as a box resting on an inclined plane, a man standing still, or an object moving with constant velocity) and unbalanced forces (such as freely falling fruit or an accelerating car)", "cs_n": 1},
            {"n": 3, "text": "draw a free-body diagram to represent the relative magnitude and direction of the forces involving balanced and unbalanced forces", "cs_n": 1},
            {"n": 4, "text": "identify that when forces are not balanced, they can cause changes in the object's speed or direction of motion", "cs_n": 1},
            {"n": 5, "text": "explain the difference between distance and displacement in everyday situations in relation to a reference point", "cs_n": 2},
            {"n": 6, "text": "distinguish between speed and velocity using the concept of vectors", "cs_n": 2},
            {"n": 7, "text": "describe uniform velocity and represent it using distance-time graphs", "cs_n": 3},
            {"n": 8, "text": "explain the difference between heat and temperature", "cs_n": 5},
            {"n": 9, "text": "identify advantageous and disadvantageous examples of conduction, convection, and radiation", "cs_n": 5},
            {"n": 10, "text": "explain in terms of the particle model the processes underlying convection and conduction of heat energy", "cs_n": 4},
            {"n": 11, "text": "gather information from secondary sources to identify and describe examples of innovative devices that can be used to transform heat energy into electrical energy", "cs_n": 5},
        ],
    },
    {
        "q": 4, "strand": "Earth and Space Science",
        "cs": [
            {"n": 1, "topic": "System models / Earthquakes", "text": "Rapid movements along normal, reverse or strike-slip faults cause earthquakes. The damage or effects on communities depend on the magnitude of and distance from an earthquake."},
            {"n": 2, "topic": "The Sun's influence on Earth", "text": "Sunlight is the Earth's external source of energy. Solar energy influences the atmosphere and weather patterns."},
            {"n": 3, "topic": "Earth's motions (revolution, rotation, tilt)", "text": "The revolution, rotation, and the tilt of the Earth explain the patterns of day and night and the seasons."},
        ],
        "lc": [
            {"n": 1, "text": "classify geological faults according to the angle of the fault plane and direction of slip", "cs_n": 1},
            {"n": 2, "text": "use models or illustrations to explain how movements along faults generate earthquakes and identify and explain which types of faults are most likely to occur in the Philippines and explain why", "cs_n": 1},
            {"n": 3, "text": "describe how the effects of earthquakes on communities depend on their magnitude", "cs_n": 1},
            {"n": 4, "text": "use the PHIVOLCS FaultFinder or other reliable information source to identify where the nearest fault system is located from their community and assess the risk of earthquakes to their local community", "cs_n": 1},
            {"n": 5, "text": "make models of fault scenarios to illustrate the epicenter of an earthquake from its focus, the intensity of an earthquake from its magnitude, and how underwater earthquakes may or may not generate tsunamis", "cs_n": 1},
            {"n": 6, "text": "refer to the local disaster readiness plans to demonstrate what to do during and after an earthquake", "cs_n": 1},
            {"n": 7, "text": "explain how earthquakes result in tsunamis that devastate shoreline communities", "cs_n": 1},
            {"n": 8, "text": "describe procedures that the authorities have in place to alert communities of pending tsunamis and what procedures can be implemented should a tsunami impact a community", "cs_n": 1},
            {"n": 9, "text": "explain how energy from the Sun interacts with the atmosphere", "cs_n": 2},
            {"n": 10, "text": "make a physical model or use drawings to demonstrate how the tilt of the Earth relative to its orbit around the Sun affects the intensity of sunlight absorbed by different areas of Earth over a year", "cs_n": 3},
            {"n": 11, "text": "explain, using models, how the tilt of the Earth affects the changes in the length of daytime at different times of the year", "cs_n": 3},
            {"n": 12, "text": "explain how solar energy contributes to the occurrence of land and sea breezes, monsoons, and the Intertropical Convergence Zone (ITCZ)", "cs_n": 2},
        ],
    },
]

# ============================================================= GRADE 8
GRADES[8] = [
    {
        "q": 1, "strand": "Life Science",
        "cs": [
            {"n": 1, "topic": "Organ systems working together", "text": "Organ systems work together for the growth and survival of the organism."},
            {"n": 2, "topic": "Heredity", "text": "Inherited traits passed from parents to offspring are governed by the rules on the patterns of inheritance."},
            {"n": 3, "topic": "Taxonomic classification", "text": "Classification of living things shows life's diversity."},
            {"n": 4, "topic": "Photosynthesis, respiration and cycles in nature", "text": "Photosynthesis and respiration are processes that show how living things obtain energy and nutrients from the environment."},
        ],
        "lc": [
            {"n": 1, "text": "using a labeled diagram, trace how food travels through the digestive tract and explain how different digestive processes work, including mechanical processing, secretion, digestion, absorption, and elimination", "cs_n": 1},
            {"n": 2, "text": "use models, flow charts, diagrams, and simulations to explain how body systems work together, such as digestion and excretion", "cs_n": 1},
            {"n": 3, "text": "describe how plant organs (leaf, stem, roots) work together as the transport system", "cs_n": 1},
            {"n": 4, "text": "represent patterns of inheritance of a simple dominant/recessive characteristic through generations of a family", "cs_n": 2},
            {"n": 5, "text": "predict simple ratios of offspring genotypes and phenotypes in crosses involving dominant/recessive gene pairs", "cs_n": 2},
            {"n": 6, "text": "describe the importance of the six-kingdom system and the three-domain system of classification of living things", "cs_n": 3},
            {"n": 7, "text": "explain why humans are classified under Class Mammalia and the Order Primates", "cs_n": 3},
            {"n": 8, "text": "using flow charts and labeled diagrams explain the role of plants and animals in the cycles of nature, such as the carbon, oxygen, and water cycles", "cs_n": 4},
            {"n": 9, "text": "describe the process of photosynthesis and respiration, and identify its raw materials needed and products", "cs_n": 4},
            {"n": 10, "text": "using information from secondary sources identify the different parts of the cell where photosynthesis and respiration occur", "cs_n": 4},
            {"n": 11, "text": "plan a scientific investigation to verify the raw materials needed for photosynthesis", "cs_n": 4},
        ],
    },
    {
        "q": 2, "strand": "Science of Materials",
        "cs": [
            {"n": 1, "topic": "Use of timelines and charts", "text": "The use of timeline and charts can illustrate scientific knowledge of the structure of the atom has evolved over time."},
            {"n": 2, "topic": "The Atomic Model", "text": "The current structure of the atom includes subatomic particles, their symbol, mass, charge, and location."},
            {"n": 3, "topic": "Subatomic particles / Elements and compounds", "text": "Elements and compounds are identified as pure substances."},
            {"n": 4, "topic": "The Periodic table", "text": "The periodic table is a useful tool to determine the chemical properties of elements."},
        ],
        "lc": [
            {"n": 1, "text": "develop a timeline for the historical background of the development of the current Atomic Model that identifies tiny particles as atoms", "cs_n": 1},
            {"n": 2, "text": "draw the structure of an atom in terms of the nucleus and electron shells", "cs_n": 2},
            {"n": 3, "text": "differentiate the subatomic particles protons, neutrons, and electrons in terms of their symbol, mass, charge, and location within an atom", "cs_n": 2},
            {"n": 4, "text": "describe the properties of pure substances as having fixed chemical composition (examples: elements and compounds), and that all the atoms of an element have a unique number of protons", "cs_n": 3},
            {"n": 5, "text": "discuss the significant contributions of early scientists in the development of the periodic table", "cs_n": 4},
            {"n": 6, "text": "identify the names and symbols of the first 20 or several common elements of the periodic table", "cs_n": 4},
            {"n": 7, "text": "explain that the arrangement of elements in the periodic table as 7 periods and 18 groups is based on their atomic structure and chemical properties, such as reactivity", "cs_n": 4},
            {"n": 8, "text": "explain that the electron structure of an atom determines its position on the periodic table", "cs_n": 4},
            {"n": 9, "text": "calculate the number of protons, neutrons, and electrons in the atom of several elements, such as aluminum", "cs_n": 2},
            {"n": 10, "text": "explain that the elements within a group in the periodic table have the same number of valence electrons", "cs_n": 4},
        ],
    },
    {
        "q": 3, "strand": "Earth and Space Science",
        "cs": [
            {"n": 1, "topic": "Distribution of the continents", "text": "The distribution of continents and oceans on Earth is related to the presence of the oceanic crust and continental crust."},
            {"n": 2, "topic": "Crustal features and interactions", "text": "Volcanic terrain is built by the slow accumulation of erupted lava. The earth's surface is made of separate and movable plates."},
            {"n": 3, "topic": "Typhoons", "text": "Bodies of water and landforms affect typhoons."},
            {"n": 4, "topic": "Tides", "text": "The interaction between the Sun, Earth, and Moon causes tides."},
        ],
        "lc": [
            {"n": 1, "text": "identify what proportion of the Earth's surface is covered with water as opposed to land", "cs_n": 1},
            {"n": 2, "text": "gather information from secondary sources to name and describe the upper crustal layers of the solid earth", "cs_n": 1},
            {"n": 3, "text": "describe the different types of volcanoes found around the world according to their activity, type of eruption, and location in the crust", "cs_n": 2},
            {"n": 4, "text": "relate the shape of a volcano's cone to its composition", "cs_n": 2},
            {"n": 5, "text": "relate the location and distribution of active volcanoes, earthquake epicenters, and major mountain belts to the distribution of oceanic crust and continental crust", "cs_n": 2},
            {"n": 6, "text": "identify how oceanic crust and continental crust is associated with the Earth's lithospheric plates", "cs_n": 2},
            {"n": 7, "text": "gather information from secondary sources to explain how typhoons develop, and why the Philippines is prone to typhoons", "cs_n": 3},
            {"n": 8, "text": "use a map and a record of tracking data to trace the path of typhoons that enter the Philippine Area of Responsibility (PAR)", "cs_n": 3},
            {"n": 9, "text": "discuss how bodies of water and landforms affect typhoons", "cs_n": 3},
            {"n": 10, "text": "gather information from the Department of Science and Technology (DOST) and other reliable websites to identify how authorities support communities affected by typhoons", "cs_n": 3},
            {"n": 11, "text": "relate the relative movements of the Earth, Moon, and Sun with the occurrence of tides", "cs_n": 4},
            {"n": 12, "text": "draw on information from secondary sources to identify situations where tidal difference could be exploited to generate renewable energy", "cs_n": 4},
        ],
    },
    {
        "q": 4, "strand": "Force, Motion, and Energy",
        "cs": [
            {"n": 1, "topic": "Acceleration", "text": "Forces cause objects to accelerate. An object is accelerating if the magnitude and/or direction of its velocity changes."},
            {"n": 2, "topic": "Distance-time and Velocity-time graphs", "text": "Kinetic energy is the energy of movement, and potential energy is stored energy."},
            {"n": 3, "topic": "Kinetic and Potential energy / Work and energy", "text": "As an object falls from a height its energy is conserved because its potential energy is transformed to kinetic energy."},
            {"n": 4, "topic": "Renewable energy", "text": "The resources of the Philippines provide many benefits to its people and their activities."},
            {"n": 5, "topic": "Properties of light", "text": "Learners describe and illustrate reflection and refraction of light."},
        ],
        "lc": [
            {"n": 1, "text": "identify that forces cause objects to accelerate, and that acceleration of an object is its rate of change of velocity", "cs_n": 1},
            {"n": 2, "text": "observe and describe examples of accelerating objects at school and in the local community, including objects that show uniform circular motion", "cs_n": 1},
            {"n": 3, "text": "construct and annotate distance-time graphs and velocity-time graphs to represent uniform and non-uniform acceleration", "cs_n": 2},
            {"n": 4, "text": "describe kinetic energy as the movement of objects or particles, and potential energy as energy stored due to the position of objects or particles", "cs_n": 3},
            {"n": 5, "text": "identify examples of everyday situations that demonstrate kinetic energy being transformed to potential energy, and potential energy being transformed to kinetic energy", "cs_n": 3},
            {"n": 6, "text": "recognize that work is done when a force causes the displacement of an object", "cs_n": 3},
            {"n": 7, "text": "recognize that power is the rate of doing work", "cs_n": 3},
            {"n": 8, "text": "explain that the mechanical energy of an object is the sum of the kinetic energy and the potential energy available to do work", "cs_n": 3},
            {"n": 9, "text": "describe conservation of energy in everyday situations involving gravity, such as when objects fall", "cs_n": 3},
            {"n": 10, "text": "gather information from secondary sources to explain how potential energy stored in lakes and dams in the Philippines is used to produce kinetic energy to generate electricity for use in homes, communities, and industry", "cs_n": 4},
            {"n": 11, "text": "carry out guided investigations to describe and illustrate the reflection of light using plane and curved mirrors and the refraction of light using transparent blocks, lenses, and prisms with examples from everyday applications", "cs_n": 5},
        ],
    },
]

# ============================================================= GRADE 9
GRADES[9] = [
    {
        "q": 1, "strand": "Force, Motion, and Energy",
        "cs": [
            {"n": 1, "topic": "Newton's Laws", "text": "Newton's laws explain and predict how objects move due to the forces that act on them."},
            {"n": 2, "topic": "Force and energy / Electric current", "text": "Electricity is a flow of electrons and can be measured and understood using current, voltage, and resistance in circuits."},
            {"n": 3, "topic": "Electrical circuits / Interpreting patterns in data", "text": "Electromagnetic radiation travels using transverse waves of different wavelengths."},
            {"n": 4, "topic": "Electromagnetic waves", "text": "Scientists and engineers use electromagnetic radiation to design modern technologies that benefit people and society."},
        ],
        "lc": [
            {"n": 1, "text": "identify inertia as the tendency for an object to stay at rest or in motion unless acted on by an unbalanced net force", "cs_n": 1},
            {"n": 2, "text": "demonstrate in practical situations and describe that acceleration is a change in speed and/or direction as the result of a net force", "cs_n": 1},
            {"n": 3, "text": "investigate the relationship among force, acceleration, and mass", "cs_n": 1},
            {"n": 4, "text": "explain that when any two objects interact, there are equal but opposite forces exerted between them, which is evident in many practical situations and applications", "cs_n": 1},
            {"n": 5, "text": "observe and identify action-reaction pairs in everyday situations such as stepping off a boat, or a book on a table, and draw force diagrams to explain how the pairs affect the motion of objects", "cs_n": 1},
            {"n": 6, "text": "identify that electricity is a flow of electrons and show appreciation for the need to observe safe measures in handling electricity", "cs_n": 2},
            {"n": 7, "text": "participate in guided investigations to infer the relationship among current, voltage, and resistance in assembled series and parallel circuits with varying number of loads and battery", "cs_n": 2},
            {"n": 8, "text": "draw diagrams of and assemble series and parallel circuits, showing switch, battery, loads/resistors, ammeter, and voltmeter", "cs_n": 3},
            {"n": 9, "text": "collaborate in a class discussion to recognize the advantages and limitations of using series or parallel circuits", "cs_n": 3},
            {"n": 10, "text": "describe electromagnetic radiation (EMR) as energy that is created by the vibrations of electrically charged particles which allows it to travel through materials or space as transverse waves", "cs_n": 4},
            {"n": 11, "text": "compare the relative wavelengths and frequencies of different types of electromagnetic waves, including radio waves, microwaves, infrared, visible light, ultra-violet, x-rays, and gamma radiation", "cs_n": 4},
            {"n": 12, "text": "identify practical applications of electromagnetic radiation, such as radio waves used in telecommunications, and x-rays and gamma rays in medicine", "cs_n": 4},
            {"n": 13, "text": "gather information from secondary sources to explain the harmful effects that EMR can have on living things", "cs_n": 4},
        ],
    },
    {
        "q": 2, "strand": "Earth and Space Science",
        "cs": [
            {"n": 1, "topic": "Scale, proportion and quantity / Plate boundaries", "text": "Evidence for continents moving includes jig-saw matching of coastlines, rock types, and the presence of similar fossils in places separated by vast distance."},
            {"n": 2, "topic": "Structure of the Earth", "text": "The movement of lithospheric plates provides a theory for understanding Earth's geological history."},
            {"n": 3, "topic": "Geologic time", "text": "The geological time scale organizes major stages in the history of the Earth over more than 4 billion years. Radioactive decay of material inside the Earth since it was formed is its internal source of energy. The Earth's interior is made up of layers of varying characteristics."},
            {"n": 4, "topic": "Origin of the Solar System", "text": "Models represent the size, structure, and relationship of components of the Solar System. Observable evidence and models help explain the nature and origin of the Solar System."},
            {"n": 5, "topic": "Space Technologies", "text": "Modern research about celestial objects uses new space technologies including telescopes and space probes."},
        ],
        "lc": [
            {"n": 1, "text": "identify and explain evidence that current continents are separate parts of what was a single continent millions of years ago", "cs_n": 1},
            {"n": 2, "text": "participate in a collaborative group or class task to examine and describe the topographical and geological evidence for plate boundaries occurring in the area where the Philippines is located", "cs_n": 1},
            {"n": 3, "text": "describe the types of plate boundaries found around the Earth", "cs_n": 1},
            {"n": 4, "text": "describe how fossils can be used for dating the age of rocks and sediments", "cs_n": 3},
            {"n": 5, "text": "describe how relative and absolute dating techniques are used to determine the subdivisions of geologic time", "cs_n": 3},
            {"n": 6, "text": "explain how the geologic time scale helps to recount the history of the Earth", "cs_n": 3},
            {"n": 7, "text": "describe how seismic wave data has been used to develop a model for the internal structure and composition of the Earth", "cs_n": 2},
            {"n": 8, "text": "create a scale drawing to represent relative thicknesses of the layers of Earth's interior, including the crust, lithosphere, asthenosphere, mantle, outer core, and inner core", "cs_n": 2},
            {"n": 9, "text": "distinguish among comets, meteoroids, asteroids, and dwarf planets, and describe how they help us to understand the nature and formation of the Earth and the Solar System", "cs_n": 4},
            {"n": 10, "text": "gather information from secondary sources to discuss the regular occurrence of meteor showers", "cs_n": 4},
            {"n": 11, "text": "explain how modern research about celestial objects uses new space technologies including telescopes and space probes", "cs_n": 5},
        ],
    },
    {
        "q": 3, "strand": "Life Science",
        "cs": [
            {"n": 1, "topic": "DNA replication and mutations", "text": "Transmission of traits is determined by DNA, genes, and chromosomes."},
            {"n": 2, "topic": "Biodiversity and endangered species", "text": "High biodiversity means populations are more likely to overcome adverse conditions."},
            {"n": 3, "topic": "Types of ecosystems in the Philippines", "text": "Human activities can adversely affect animals and plants in a variety of ecosystems."},
        ],
        "lc": [
            {"n": 1, "text": "use models and labeled diagrams to represent the double helix structure of DNA (deoxyribonucleic acid)", "cs_n": 1},
            {"n": 2, "text": "explain the role of DNA, genes, and chromosomes in the transmission of traits", "cs_n": 1},
            {"n": 3, "text": "describe mutations as changes in DNA or chromosomes and discuss some of the factors that cause mutations, such as infectious agents, radiation, and chemicals", "cs_n": 1},
            {"n": 4, "text": "use information from secondary sources to explain the beneficial, harmful, and neutral effects of mutations", "cs_n": 1},
            {"n": 5, "text": "explain the advantage of high biodiversity in maintaining the stability of an ecosystem during difficult conditions, such as food shortages, disease, and climate change", "cs_n": 2},
            {"n": 6, "text": "use information from secondary resources to classify animals and plants of the Philippines as critically endangered, endangered, or vulnerable species", "cs_n": 2},
            {"n": 7, "text": "discuss as a class how threats to biodiversity can lead to species extinction", "cs_n": 2},
            {"n": 8, "text": "use information from secondary sources to research how to protect and conserve endangered and/or economically important species in the local community", "cs_n": 2},
            {"n": 9, "text": "describe using labeled diagrams the biotic and abiotic features of tropical rainforests, swamps, estuaries, mangrove forests, and coral reefs", "cs_n": 3},
            {"n": 10, "text": "use information from secondary sources to describe the possible effects of human activities, such as deforestation, pollution, and introduction of invasive species, on living things in an ecosystem", "cs_n": 3},
            {"n": 11, "text": "plan to conduct a survey to explore the possibilities for minimizing the negative impacts of human activities on an ecosystem", "cs_n": 3},
        ],
    },
    {
        "q": 4, "strand": "Science of Materials",
        "cs": [
            {"n": 1, "topic": "Valid and reliable investigations", "text": "Valid and reliable scientific investigations include identification and control of variables."},
            {"n": 2, "topic": "Chemical bonding", "text": "Formation or breaking down of ionic or covalent bonds results in a chemical change."},
            {"n": 3, "topic": "Ionic compounds", "text": "Bonds are formed between atoms either by sharing or transferring of electrons."},
            {"n": 4, "topic": "Covalent compounds", "text": "The type of bond formed determines whether the result is a covalent or ionic compound."},
            {"n": 5, "topic": "Metallic bonds", "text": "Symbols for the elements are used as a basis for writing chemical formula of compounds."},
            {"n": 6, "topic": "Chemical formula", "text": "The properties of pure substances depend on the type of bonding within them."},
        ],
        "lc": [
            {"n": 1, "text": "carry out a valid and reliable scientific investigation to show the formation of a new substance, such as formation of a carbonate (carbon dioxide in limewater), or formation of a precipitate (from silver nitrate solution)", "cs_n": 1},
            {"n": 2, "text": "explain that the formation of new bonds or the breaking of existing bonds constitutes a chemical change and the formation of a new substance", "cs_n": 2},
            {"n": 3, "text": "describe a valence electron as an electron in the outer shell of an atom that can take part in formation of bonds", "cs_n": 3},
            {"n": 4, "text": "identify the number of valence electrons of oxygen based on its position in the periodic table", "cs_n": 3},
            {"n": 5, "text": "explain the formation of ions as either the loss or gain of electrons to produce ionic bonds, using examples, such as the formation of sodium chloride", "cs_n": 3},
            {"n": 6, "text": "write the chemical formula and chemical names of some common ionic compounds, including sodium chloride (NaCl), magnesium oxide (MgO), potassium chloride (KCl) and magnesium chloride (MgCl2)", "cs_n": 6},
            {"n": 7, "text": "explain the formation of covalent bonds using a molecule of water and a molecule of carbon dioxide", "cs_n": 4},
            {"n": 8, "text": "write the chemical formula and chemical name of some common covalent compounds, including water (H2O), carbon dioxide (CO2), and ammonia (NH3)", "cs_n": 6},
            {"n": 9, "text": "show by using models that ionic compounds form crystalline structures whereas covalent compounds form individual molecules", "cs_n": 4},
            {"n": 10, "text": "explain properties of metals in terms of their structure and metallic bonding (sea of electrons model)", "cs_n": 5},
            {"n": 11, "text": "investigate the properties of ionic, covalent, and metallic substances, such as melting point, hardness, electrical and thermal conductivity", "cs_n": 5},
        ],
    },
]

# ============================================================= GRADE 10
GRADES[10] = [
    {
        "q": 1, "strand": "Earth and Space Science",
        "cs": [
            {"n": 1, "topic": "Plate Tectonics", "text": "Current models explain tectonic plate movement as part of a gravity-driven convection system that pushes young hot plates away from spreading ridges and pulls old cold plates down into subduction zones."},
            {"n": 2, "topic": "Global climate", "text": "Plate movements and continental evolution account for the major surface features of the Earth."},
            {"n": 3, "topic": "Global interactions", "text": "Climate change and its impacts on the environment and people pose serious challenges which require solutions and action at local and global levels."},
            {"n": 4, "topic": "Global and local Sustainability", "text": "The rich natural resources of the Philippines require sustainable management."},
        ],
        "lc": [
            {"n": 1, "text": "identify modern scientific processes used to detect and measure the displacement of tectonic plates", "cs_n": 1},
            {"n": 2, "text": "describe the structures, movements and events that occur at each type of plate boundary", "cs_n": 1},
            {"n": 3, "text": "identify the locations of major mountains, faults, volcanos, and ocean trenches using a map of the Philippine Archipelago, and interpret the features in relation to plate tectonics", "cs_n": 1},
            {"n": 4, "text": "predict the position and shape of the Philippine Archipelago in 50 million years, based on the current velocity of the Philippine Plate", "cs_n": 1},
            {"n": 5, "text": "gather information from secondary sources to describe and explain what mechanisms that drive the movement of tectonic plates including the role of the asthenosphere", "cs_n": 2},
            {"n": 6, "text": "explain how the subduction of an oceanic plate impacts on the plate above it", "cs_n": 2},
            {"n": 7, "text": "explain how plate tectonics can be used to explain the formation of the largest mountain ranges on Earth including the Himalayas and the Andes mountains", "cs_n": 2},
            {"n": 8, "text": "identify evidence of global warming and climate change", "cs_n": 3},
            {"n": 9, "text": "identify the role of greenhouse gases in enhanced global warming and climate change", "cs_n": 3},
            {"n": 10, "text": "describe how global climatic phenomena, such as the El Ni\u00f1o Southern Oscillation, may impact weather systems", "cs_n": 3},
            {"n": 11, "text": "identify local impacts of global climate change and suggest ways that individuals can do to reduce the impact of global warming", "cs_n": 3},
            {"n": 12, "text": "explain how increased societal uses of renewable energies could mitigate the effects of global climate change, including how the Philippines could make better use of its plentiful natural resources", "cs_n": 4},
        ],
    },
    {
        "q": 2, "strand": "Force, Motion, and Energy",
        "cs": [
            {"n": 1, "topic": "Projectile motion", "text": "Newton's laws can be used to explain projectile motion and collisions."},
            {"n": 2, "topic": "Momentum and Collisions", "text": "Momentum in collisions increases as mass or velocity increases."},
            {"n": 3, "topic": "Large-scale generation and distribution of electricity", "text": "The electric companies provide high voltage electricity through power generation, transmission, and distribution to many parts of the archipelago."},
            {"n": 4, "topic": "Renewable and non-renewable energy", "text": "Responsible planning and innovation lead to efficient generation and distribution of electricity in the Philippines."},
        ],
        "lc": [
            {"n": 1, "text": "investigate and describe the relationship among the projectile variables including the angle and velocity of release, and projectile height and range, using everyday activities such as shooting basketballs or kicking footballs", "cs_n": 1},
            {"n": 2, "text": "describe different types of collisions as elastic or inelastic by providing some examples", "cs_n": 2},
            {"n": 3, "text": "use models to investigate elastic or inelastic collisions and describe the forces involved and their effects", "cs_n": 2},
            {"n": 4, "text": "explain that momentum depends on the mass and the velocity of a moving object that can be used to predict the impact the object will have if it hits another object", "cs_n": 2},
            {"n": 5, "text": "carry out guided investigations using different objects to describe momentum-related relationships, such as the more momentum an object has, the harder for it to stop", "cs_n": 2},
            {"n": 6, "text": "identify and explain that to change the momentum of an object, it is necessary to apply a force on the object over a period of time", "cs_n": 2},
            {"n": 7, "text": "gather information from secondary sources to identify ways to reduce the impact of collisions such as seatbelts, airbags, and crumple zones in vehicles", "cs_n": 2},
            {"n": 8, "text": "identify that momentum is conserved before and after the collision of objects", "cs_n": 2},
            {"n": 9, "text": "describe how high voltage electricity from power plants is generated and safely distributed to industries, businesses, and homes, including the role of substations (grid stations), and electric meters", "cs_n": 3},
            {"n": 10, "text": "describe and explain the need for safety precautions in handling household electrical devices", "cs_n": 3},
            {"n": 11, "text": "describe the similarities and differences between electric motors and electric generators", "cs_n": 3},
            {"n": 12, "text": "collaborate in a class discussion to identify ways to reduce the use of electrical energy in Filipino houses and communities and explain what local and global benefits can be achieved", "cs_n": 4},
            {"n": 13, "text": "gather information from secondary sources to evaluate how renewable and non-renewable generation of electricity in the Philippines impacts human activities and the environment", "cs_n": 4},
        ],
    },
    {
        "q": 3, "strand": "Science of Materials",
        "cs": [
            {"n": 1, "topic": "Chemical reactions", "text": "Several simple observations indicate if a chemical reaction has taken place."},
            {"n": 2, "topic": "Acids, bases, and salts", "text": "Chemical indicators produce color changes with acids, bases, and salts."},
            {"n": 3, "topic": "Types of chemical reactions", "text": "Valid and reliable scientific investigations identify the dependent and independent variables and control other variables. Many types of chemical reactions are important in our daily lives and in the biotic and abiotic parts of the environment."},
            {"n": 4, "topic": "Chemical reactions in the environment / Chemical equations", "text": "Atoms rearrange during chemical reactions but abide by the principle of conservation of mass as illustrated in balanced chemical equations."},
            {"n": 5, "topic": "Rates of reactions", "text": "Rates of chemical reactions are critical in production and preservation of many useful materials."},
        ],
        "lc": [
            {"n": 1, "text": "describe the indicators for a chemical reaction as color change, the formation of a precipitate, the release of gas, and or odor, or a change in temperature", "cs_n": 1},
            {"n": 2, "text": "identify common acids, bases, and salts (e.g., hydrochloric acid, sodium hydroxide, and saline solution) using different indicators", "cs_n": 2},
            {"n": 3, "text": "describe important types of chemical reactions (combination, decomposition, single replacement, double replacement)", "cs_n": 3},
            {"n": 4, "text": "explain how important types of chemical reactions, such as combustion, acids on metals, acids on carbonates, photosynthesis, and respiration, relate to or impact the natural and built environments using information from secondary sources", "cs_n": 3},
            {"n": 5, "text": "recognize that scientists use chemical equations to describe chemical reactions, and write equations in word form and using formula for common chemical reactions", "cs_n": 4},
            {"n": 6, "text": "explain that chemical equations demonstrate a rearrangement of atoms but the total mass of the system remains the same during a chemical reaction", "cs_n": 4},
            {"n": 7, "text": "apply the principles of conservation of mass to balance chemical equations", "cs_n": 4},
            {"n": 8, "text": "explain the factors affecting the rates of chemical reactions as applied in food preservation and materials production, control of fire, pollution, and corrosion", "cs_n": 5},
            {"n": 9, "text": "identify that chemical reactions may be exothermic or endothermic", "cs_n": 5},
        ],
    },
    {
        "q": 4, "strand": "Life Science",
        "cs": [
            {"n": 1, "topic": "Homeostasis", "text": "Homeostasis is a self-regulating process that allows an organism to maintain stability."},
            {"n": 2, "topic": "Mechanisms of evolution", "text": "Several theories provide lines of evidence about how organisms evolve."},
            {"n": 3, "topic": "Biotechnology", "text": "The products and processes of biotechnology can have both beneficial and harmful effects on society and the environment."},
            {"n": 4, "topic": "Ecosystem's carrying capacity and population growth", "text": "Population growth influences the carrying capacity of an ecosystem."},
        ],
        "lc": [
            {"n": 1, "text": "describe homeostasis as a state of balance among all the body systems in humans that needs to be maintained for survival and proper functioning; its indicators include body temperature, glucose level, and blood pressure", "cs_n": 1},
            {"n": 2, "text": "explain how homeostasis is maintained through various feedback mechanisms, both positive and negative", "cs_n": 1},
            {"n": 3, "text": "use information from secondary sources to describe natural selection as the primary mechanism driving evolutionary change", "cs_n": 2},
            {"n": 4, "text": "discuss in small groups important concepts in the theories of evolution, such as variation, heredity, isolation, selection, and adaptation", "cs_n": 2},
            {"n": 5, "text": "use information from secondary sources to explain how lines of evidence, such as fossils, biogeography, and comparative morphology, support the occurrence of evolution", "cs_n": 2},
            {"n": 6, "text": "explain the term biotechnology and provide examples", "cs_n": 3},
            {"n": 7, "text": "use information from secondary sources to identify the products of traditional biotechnology through fermentation (e.g. cheese, soy sauce, vinegar, nata de coco)", "cs_n": 3},
            {"n": 8, "text": "use information from secondary sources to identify examples of modern biotechnology, such as genetically modified organisms and processes (e.g. in vitro fertilization)", "cs_n": 3},
            {"n": 9, "text": "participate in a class debate on the societal, environmental, and ethical implications of using biotechnological products and methods", "cs_n": 3},
            {"n": 10, "text": "discuss the factors that limit the ecosystem's carrying capacity, such as adequate food, shelter, water, and mates", "cs_n": 4},
            {"n": 11, "text": "explain that the ecosystem's population growth slows down as it gets closer to the carrying capacity", "cs_n": 4},
        ],
    },
]

print("All grades loaded:", list(GRADES.keys()))
print({g: sum(len(q['lc']) for q in qs) for g, qs in GRADES.items()})
print("Total LCs:", sum(sum(len(q['lc']) for q in qs) for qs in GRADES.values()))

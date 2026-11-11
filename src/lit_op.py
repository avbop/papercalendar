from events import event
from colors import Color
from icons import Icon

HOLY_NAME = event("Most Holy Name of Jesus (II)", Color.WHITE, Icon.OP)
EPIPHANY = event("Epiphany of the Lord (I)", Color.WHITE, Icon.OP)
BAPTISM = event("Baptism of the Lord (II)", Color.WHITE, Icon.OP)
CROWN = event("Crown of Thorns (III)", Color.RED, Icon.OP)
CORPUS = event("Corpus Christi (I)", Color.WHITE, Icon.OP)
SACRED_HEART = event("Most Sacred Heart of Jesus (I)", Color.WHITE, Icon.OP)
SANGUIS = event("Sanguis Christi (I)", Color.RED, Icon.OP)

CO = event("Christmas Octave (II)", Color.WHITE, Icon.OP)
CO_SUN = event("Sunday in the Octave (II)", Color.WHITE, Icon.OP)
CO_8 = event("Octave Day of the Nativity (I)", Color.WHITE, Icon.OP)
CF = event("Feria (IV)", Color.WHITE, Icon.OP)
HOLY_FAMILY = event("Holy Family (II)", Color.WHITE, Icon.OP)
AEF = event("Feria (IV)", Color.GREEN, Icon.OP)
AE2 = event(
    "Second Sunday after Epiphany (II)\n(Sunday I after Octave)",
    Color.GREEN,
    Icon.OP,
)
AE3 = event(
    "Third Sunday after Epiphany (II)\n(Sunday II after Octave)",
    Color.GREEN,
    Icon.OP,
)
L70 = event("Septuagesima Sunday (II)", Color.PURPLE, Icon.OP)
L60 = event("Sexagesima Sunday (II)", Color.PURPLE, Icon.OP)
L50 = event("Quinquagesima Sunday (II)", Color.PURPLE, Icon.OP)
ASH_WEDNESDAY = event("Ash Wednesday (I)", Color.PURPLE, Icon.OP)
LF = event("Feria (III)", Color.PURPLE, Icon.OP)
L1 = event("First Sunday of Lent (I)", Color.PURPLE, Icon.OP)
L2 = event("Second Sunday of Lent (I)", Color.PURPLE, Icon.OP)
L3 = event("Third Sunday of Lent (I)", Color.PURPLE, Icon.OP)
L4 = event("Fourth Sunday of Lent (I)", Color.PINK, Icon.OP)
PASSION = event("Passion Sunday (I)", Color.PURPLE, Icon.OP)
L5 = PASSION
PALM = event("Palm Sunday (I)", Color.PURPLE, Icon.OP)
L6 = PALM
HOLY_WEEK_MON = event("Monday of Holy Week (I)", Color.PURPLE, Icon.OP)
HOLY_WEEK_TUE = event("Tuesday of Holy Week (I)", Color.PURPLE, Icon.OP)
HOLY_WEEK_WED = event("Wednesday of Holy Week (I)", Color.PURPLE, Icon.OP)
HOLY_THURSDAY = event("Holy Thursday (I)", Color.WHITE, Icon.OP)
GOOD_FRIDAY = event("Good Friday (I)", Color.BLACK, Icon.OP)
HOLY_SATURDAY = event("Holy Saturday (I)", Color.WHITE, Icon.OP)
EASTER = event("Easter Sunday (I)", Color.WHITE, Icon.OP)
E0 = EASTER
EO = event("Easter Octave (I)", Color.WHITE, Icon.OP)
EO_SUN = event("Octave of the Resurrection (I)", Color.WHITE, Icon.OP)
E1 = EO_SUN
EF = event("Feria (IV)", Color.WHITE, Icon.OP)
E2 = event(
    "Second Sunday after Easter (II)\n(Sunday I after Octave)", Color.WHITE, Icon.OP
)
E3 = event(
    "Third Sunday after Easter (II)\n(Sunday II after Octave)", Color.WHITE, Icon.OP
)
E4 = event(
    "Fourth Sunday after Easter (II)\n(Sunday III after Octave)",
    Color.WHITE,
    Icon.OP,
)
E5 = event(
    "Fifth Sunday after Easter (II)\n(Sunday IV after Octave)", Color.WHITE, Icon.OP
)
ASCENSION_VIGIL = event("Vigil of the Ascension (II)", Color.WHITE, Icon.OP)
ASCENSION = event("Ascension of the Lord (I)", Color.WHITE, Icon.OP)
ASCENSION_SUN = event(
    "Sunday after the Ascension (II)\n(Sunday in the Octave of Ascension)",
    Color.WHITE,
    Icon.OP,
)
PENTECOST_VIGIL = event("Vigil of Pentecost (I)", Color.RED, Icon.OP)
PENTECOST = event("Pentecost (I)", Color.RED, Icon.OP)
PO = event("Pentecost Octave (I)", Color.RED, Icon.OP)
TRINITY = event("Trinity Sunday (I)", Color.WHITE, Icon.OP)
AP2 = event(
    "Second Sunday after Pentecost (II)\n(Sunday in the Octave of Corpus Christi)",
    Color.GREEN,
    Icon.OP,
)
AP3 = event(
    "Third Sunday after Pentecost (II)\n(Sunday in the Octave of the Sacred Heart)",
    Color.GREEN,
    Icon.OP,
)
AP4 = event(
    "Fourth Sunday after Pentecost (II)\n(Sunday II after Octave)",
    Color.GREEN,
    Icon.OP,
)
AP5 = event(
    "Fifth Sunday after Pentecost (II)\n(Sunday III after Octave)",
    Color.GREEN,
    Icon.OP,
)
AP6 = event(
    "Sixth Sunday after Pentecost (II)\n(Sunday IV after Octave)",
    Color.GREEN,
    Icon.OP,
)
AP7 = event(
    "Seventh Sunday after Pentecost (II)\n(Sunday V after Octave)",
    Color.GREEN,
    Icon.OP,
)

BVM = event("Our Lady on Saturday (IV)", Color.WHITE, Icon.OP)
PURIFICATION_BVM = event("Purification of Our Lady (II)", Color.WHITE, Icon.OP)
APPARITION_BVM = event("Apparition of Our Lady (III)", Color.WHITE, Icon.OP)
ANNUNCIATION = event("Annunciation of Our Lady (I)", Color.WHITE, Icon.OP)
COMPASSION_BVM = event("Compassion of Our Lady (m)", Color.WHITE, Icon.OP)
MEDIATRIX = event("Our Lady, Mediatrix of all Graces (III)", Color.WHITE, Icon.OP)
QUEEN = event("Our Lady, Queen (III)", Color.WHITE, Icon.OP)
VISITATION = event("Visitation of Our Lady (II)", Color.WHITE, Icon.OP)

EMBER_W = event("Ember Wednesday (II)", Color.PURPLE, Icon.OP)
EMBER_F = event("Ember Friday (II)", Color.PURPLE, Icon.OP)
EMBER_S = event("Ember Saturday (II)", Color.PURPLE, Icon.OP)
EMBER_W_P = event("Ember Wednesday (I)", Color.RED, Icon.OP)
EMBER_F_P = event("Ember Friday (I)", Color.RED, Icon.OP)
EMBER_S_P = event("Ember Saturday (I)", Color.RED, Icon.OP)

ZEDISLAVA = event("St. Zedislava (III)", Color.WHITE, Icon.OP)
HILARY = event("St. Hilary (III)", Color.WHITE, Icon.OP)
FELIX = event("St. Felix (m)", Color.RED, Icon.OP)
FRANCIS_CAPILLAS = event("St. Francis de Capillas (III)", Color.RED, Icon.OP)
MAURUS = event("St. Maurus (m)", Color.WHITE, Icon.OP)
PAUL_HERMIT = event("St. Paul the first hermit (m)", Color.WHITE, Icon.OP)
MARCELLUSI = event("St. Marcellus I (m)", Color.RED, Icon.OP)
ANTHONY = event("St. Anthony (III)", Color.WHITE, Icon.OP)

JOHN = event("St. John (I)", Color.WHITE, Icon.OP)
HOLY_INNOCENTS = event("Holy Innocents (II)", Color.RED, Icon.OP)
THOMAS_BECKET = event("St. Thomas Becket (III)", Color.RED, Icon.OP)
SYLVESTER = event("St. Sylvester I (III)", Color.WHITE, Icon.OP)
MARGARET_HUNGARY = event("St. Margaret of Hungary (III)", Color.WHITE, Icon.OP)
PRISCA = event("St. Prisca (m)", Color.RED, Icon.OP)
FABIAN_SEBASTIAN = event("Ss. Fabian and Sebastian (III)", Color.RED, Icon.OP)
AGNES = event("St. Agnes (III)", Color.RED, Icon.OP)
VINCENT = event("St. Vincent (III)", Color.RED, Icon.OP)
RAYMOND_PEÑAFORT = event("St. Raymond of Peñafort (III)", Color.WHITE, Icon.OP)
EMERENTIANA = event("St. Emerentiana (m)", Color.RED, Icon.OP)
TIMOTHY = event("St. Timothy (m)", Color.RED, Icon.OP)
POLYCARP = event("St. Timothy (m)", Color.RED, Icon.OP)
JOHN_CHRYSOSTOM = event("St. John Chrysostom (III)", Color.WHITE, Icon.OP)
JULIAN = event("St. Julian (m)", Color.WHITE, Icon.OP)
PETER_NOLASCUS = event("St. Peter Nolascus (III)", Color.WHITE, Icon.OP)
FRANCIS_SALES = event("St. Francis de Sales (III)", Color.WHITE, Icon.OP)
MARTINA = event("St. Martina (m)", Color.RED, Icon.OP)
JOHN_BOSCO = event("St. John Bosco (III)", Color.WHITE, Icon.OP)
BLAISE = event("St. Blaise (m)", Color.RED, Icon.OP)
ANDREW_CORSINI = event("St. Andrew Corsini (III)", Color.WHITE, Icon.OP)
AGATHA = event("St. Agatha (III)", Color.RED, Icon.OP)
VEDAST_AMAND = event("Ss. Vedast and Amand (IV)", Color.WHITE, Icon.OP)
ROMUALD = event("St. Romuald (III)", Color.WHITE, Icon.OP)
CYRIL_ALEXANDRIA = event("St. Cyril of Alexandria (III)", Color.WHITE, Icon.OP)
SCHOLASTICA = event("St. Scholastica (III)", Color.WHITE, Icon.OP)
SEVEN_FOUNDERS = event("Seven Holy Servite Founders (III)", Color.WHITE, Icon.OP)
CATHERINE_RICCI = event("St. Catherine de Ricci (III)", Color.WHITE, Icon.OP)
JORDAN_SAXONY = event("St. Jordan of Saxony (III)", Color.WHITE, Icon.OP)
VALENTINE = event("St. Valentine (m)", Color.RED, Icon.OP)
REGINALD = event("Bl. Reginald (m)", Color.WHITE, Icon.OP)
JOHN_FIESOLE = event("Bl. John of Fiesole (m)", Color.WHITE, Icon.OP)
CHAIR_PETER = event("Chair of St. Peter (II)", Color.WHITE, Icon.OP)
PETER_DAMIAN = event("St. Peter Damian (III)", Color.WHITE, Icon.OP)
MATTHIAS = event("St. Matthias (II)", Color.RED, Icon.OP)
CASIMIR = event("St. Casimir (III)", Color.WHITE, Icon.OP)
THOMAS_AQUINAS = event("St. Thomas Aquinas (I)", Color.WHITE, Icon.OP)
JOHN_GOD = event("St. John of God (III)", Color.WHITE, Icon.OP)
FRANCES_ROME = event("St. Frances of Rome (III)", Color.WHITE, Icon.OP)
GREGORY = event("St. Gregory the Great (III)", Color.WHITE, Icon.OP)
PATRICK = event("St. Patrick (III)", Color.WHITE, Icon.OP)
CYRIL_JERUSALEM = event("St. Cyril of Jerusalem (III)", Color.WHITE, Icon.OP)
JOSEPH = event("St. Joseph (I)", Color.WHITE, Icon.OP)
AMBROSE_SANSEDONIUS = event("Bl. Ambrose Sansedonius (m)", Color.WHITE, Icon.OP)
BENEDICT = event("St. Benedict (III)", Color.WHITE, Icon.OP)
GABRIEL = event("St. Gabriel (III)", Color.WHITE, Icon.OP)
JOHN_DAMASCENE = event("St. John Damascene (III)", Color.WHITE, Icon.OP)
LEO = event("St. Leo the Great (III)", Color.WHITE, Icon.OP)
TIBURTIUS = event("Ss. Tiburtius, Valerian, and Maximus (m)", Color.RED, Icon.OP)
AGNES_MONTEPULCIANO = event("St. Agnes of Montepulciano (III)", Color.WHITE, Icon.OP)
ANSELM = event("St. Anselm (III)", Color.WHITE, Icon.OP)
GEORGE = event("St. George (m)", Color.RED, Icon.OP)
MARK = event("St. Mark (II)\nGreater Litanies", Color.RED, Icon.OP)
PAUL_CROSS = event("St. Paul of the Cross (III)", Color.WHITE, Icon.OP)
LOUIS_MONTFORT = event("St. Louis de Montfort (m)", Color.WHITE, Icon.OP)
PETER_MARTYR = event("St. Peter Martyr (II)", Color.RED, Icon.OP)
CATHERINE_SIENA = event("St. Catherine of Siena (II)", Color.WHITE, Icon.OP)
JOSEPH = event("St. Joseph (I)", Color.WHITE, Icon.OP)
ATHANASIUS = event("St. Athanasius (III)", Color.WHITE, Icon.OP)
ALEXANDER = event("Ss. Alexander, Eventius, and Theodulus (m)", Color.RED, Icon.OP)
MONICA = event("St. Monica (III)", Color.WHITE, Icon.OP)
PIUSV = event("St. Pius V (III)", Color.WHITE, Icon.OP)
STANISLAUS = event("St. Stanislaus (III)", Color.RED, Icon.OP)
GREGORY_NAZIANZEN = event("St. Gregory Nazianzen (III)", Color.WHITE, Icon.OP)
ANTONINUS = event("St. Antoninus (III)", Color.WHITE, Icon.OP)
GORDIAN = event("Ss. Gordian and Epimachus (m)", Color.RED, Icon.OP)
PHILIP_JAMES = event("Ss. Philip and James (II)", Color.RED, Icon.OP)
NEREUS = event("Ss. Nereus, Achilleus, and Pancras (m)", Color.RED, Icon.OP)
IMELDA = event("Bl. Imelda (m)", Color.WHITE, Icon.OP)
JOHN_BAPTIST_DE_LA_SALLE = event(
    "St. John Baptist de la Salle (III)", Color.WHITE, Icon.OP
)
VENANTIUS = event("St. Venantius (III)", Color.RED, Icon.OP)
PETER_CELESTINE = event("St. Peter Celestine (III)", Color.WHITE, Icon.OP)
PUDENTIANA = event("St. Pudentiana (m)", Color.WHITE, Icon.OP)
DOMINIC_TRANSLATION = event(
    "Translation of Our Holy Father Dominic (III)", Color.WHITE, Icon.OP
)
URBANI = event("St. Urban I (III)", Color.RED, Icon.OP)
PHILIP_NERI = event("St. Philip Neri (III)", Color.WHITE, Icon.OP)
BEDE = event("St. Bede the Venerable (III)", Color.WHITE, Icon.OP)
WILLIAM = event("Bls. William and companions (m)", Color.RED, Icon.OP)
PETRONILLA = event("St. Petronilla (III)", Color.WHITE, Icon.OP)
ANGELA_MERICI = event("St. Angela Merici (m)", Color.WHITE, Icon.OP)
SADOC = event("Bls. Sadoc and companions (m)", Color.RED, Icon.OP)
MARCELLINUS_PETER = event("Ss. Marcellinus and Peter (m)", Color.RED, Icon.OP)
PETER_SANZ = event("Ss. Peter Sanz and companions (m)", Color.RED, Icon.OP)
FRANCIS_CARACCIOLO = event("St. Francis Caracciolo (m)", Color.WHITE, Icon.OP)
NORBERT = event("St. Norbert (III)", Color.WHITE, Icon.OP)
MEDARD = event("St. Medard (m)", Color.WHITE, Icon.OP)
DIANA = event("Bls. Diana, Cecilia, and Amata (m)", Color.WHITE, Icon.OP)
PRIMUS = event("Ss. Primus and Felician (m)", Color.RED, Icon.OP)
JOHN_DOMINIC = event("Bl. John Dominic (m)", Color.WHITE, Icon.OP)
BARNABAS = event("St. Barnabas (III)", Color.RED, Icon.OP)
BASILIDES = event("Ss. Basilides, Cyrinus, Nabor, and Nazarius (m)", Color.RED, Icon.OP)
ANTHONY_PADUA = event("St. Anthony of Padua (III)", Color.WHITE, Icon.OP)
BASIL = event("St. Basil the Great (III)", Color.WHITE, Icon.OP)
VITUS = event("Ss. Vitus, Modest, and Crescentia (m)", Color.RED, Icon.OP)
QUIRICUS = event("Ss. Quiricus and Julitta (m)", Color.RED, Icon.OP)
EPHREM = event("St. Ephrem the Syrian (III)", Color.WHITE, Icon.OP)
MARK_MARCELLIAN = event("Ss. Mark and Marcellian (m)", Color.RED, Icon.OP)
GERVASE = event("Ss. Gervase and Protasus (m)", Color.RED, Icon.OP)
INNOCENTV = event("Bl. Innocent V (m)", Color.WHITE, Icon.OP)
BAPTIST_NATIVITY_VIGIL = event(
    "Vigil of the Nativity of St. John the Baptist (II)", Color.PURPLE, Icon.OP
)
BAPTIST_NATIVITY = event("Nativity of St. John the Baptist (I)", Color.WHITE, Icon.OP)
JOHN_PAUL = event("Ss. John and Paul (III)", Color.RED, Icon.OP)
PETER_PAUL = event("Ss. Peter and Paul (I)", Color.RED, Icon.OP)
PAUL = event("St. Paul (III)", Color.RED, Icon.OP)
PROCESSUS = event("Ss. Processus and Martinian (m)", Color.RED, Icon.OP)
IRENAEUS = event("St. Irenaeus (III)", Color.RED, Icon.OP)
ANTHONY_ZACCARIA = event("St. Anthony Mary Zaccaria (III)", Color.WHITE, Icon.OP)
BENEDICTXI = event("Bl. Benedict XI (m)", Color.WHITE, Icon.OP)
FISHER_MORE = event("Ss. John Fisher and Thomas More (III)", Color.RED, Icon.OP)
SEVEN_BROTHERS = event("Seven Holy Brothers (III)", Color.RED, Icon.OP)
IGNATIUS_DELGADO = event(
    "Ss. Ignatius Delgado, Dominic Henares, and companions (m)", Color.RED, Icon.OP
)
JOHN_GUALBERT = event("St. John Gualbert (III)", Color.WHITE, Icon.OP)

PARENTS = event("Deceased Parents", Color.BLACK, Icon.OP)
CEMETERIES = event("Those buried in our cemeteries", Color.BLACK, Icon.OP)

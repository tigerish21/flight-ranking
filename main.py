from src.load_data import load_train_data

columns = [    # Dati utente / sessione
    "ranker_id",
    "profileId",
    "sex",
    "requestDate",
    "searchRoute",

    # Target / variabili di risposta
    "selected",
    "totalPrice",

    # Tariffa e compagnia
    "companyID",
    "corporateTariffCode",
    "pricingInfo_isAccessTP",
    "pricingInfo_passengerCount",

    # Status / privilegi
    "frequentFlyer",
    "isVip",
    "isAccess3D",

    # Informazioni sui voli e segmenti
    "legs0_arrivalAt",
    "legs0_departureAt",
    "legs0_duration",
    "legs0_segments0_aircraft_code",
    "legs0_segments0_marketingCarrier_code",
    "legs0_segments0_operatingCarrier_code",
    "legs0_segments0_seatsAvailable",
    "legs0_segments0_baggageAllowance_quantity",
    "legs0_segments0_baggageAllowance_weightMeasurementType",
    
    "legs1_arrivalAt",
    "legs1_departureAt",
    "legs1_duration",
    "legs1_segments0_aircraft_code",
    "legs1_segments0_marketingCarrier_code",
    "legs1_segments0_operatingCarrier_code",
    "legs1_segments0_seatsAvailable",
    "legs1_segments0_baggageAllowance_quantity",
    "legs1_segments0_baggageAllowance_weightMeasurementType",

    # MiniRules (sconti o regole tariffarie)
    "miniRules0_monetaryAmount",
    "miniRules0_percentage",
    "miniRules0_statusInfos",
    "miniRules1_monetaryAmount",
    "miniRules1_percentage",
    "miniRules1_statusInfos"
]

df =load_train_data(columns_to_use=columns, sample_size=4000)

print(df.info())











# Info app - Product constants
# ----------------------------------------------------------------------------
# product type choices
PRODUCT_TYPE_GASOLINE = 'gas'
PRODUCT_TYPE_OIL = 'oil'
PRODUCT_TYPE = (
    (PRODUCT_TYPE_GASOLINE, 'Gas'),
    (PRODUCT_TYPE_OIL, 'Oil')
)

# duration unit choices
DURATION_UNIT_MINITE = 'M'
DURATION_UNIT_HOUR = 'H'
DURATION_UNIT = (
    (DURATION_UNIT_MINITE, 'Minute'),
    (DURATION_UNIT_HOUR, 'Hour'),
)


# Vehicle app - Vehicle constants
# ----------------------------------------------------------------------------
# vehicle model choices
VEHICLE_MODEL_TYPE_TRUCK = 'T'
VEHICLE_MODEL_TYPE_SEMI_TRAILER = 'S'
VEHICLE_MODEL_TYPE = (
    (VEHICLE_MODEL_TYPE_TRUCK, 'Truck'),
    (VEHICLE_MODEL_TYPE_SEMI_TRAILER, 'Semi-trailer')
)

# vehicle brand choices
VEHICLE_BRAND_TONGHUA = 'T'
VEHICLE_BRAND_LIBERATION = 'L'
VEHICLE_BRAND_YANGZHOU = 'Y'
VEHICLE_BRAND = (
    (VEHICLE_BRAND_TONGHUA, 'Tonghua'),
    (VEHICLE_BRAND_LIBERATION, 'Liberation'),
    (VEHICLE_BRAND_YANGZHOU, 'Yangzhou')
)

# vehicle document type choices
VEHICLE_DOCUMENT_TYPE_D1 = '1'
VEHICLE_DOCUMENT_TYPE_D2 = '2'
VEHICLE_DOCUMENT_TYPE = (
    (VEHICLE_DOCUMENT_TYPE_D1, 'D1'),
    (VEHICLE_DOCUMENT_TYPE_D2, 'D2')
)


# Account app - Account constants
# ----------------------------------------------------------------------------
# user role choices
USER_ROLE_ADMIN = 'A'
USER_ROLE_STAFF = 'S'
USER_ROLE_DRIVER = 'D'
USER_ROLE_ESCORT = 'E'
USER_ROLE_CUSTOMER = 'C'
USER_ROLE = (
    (USER_ROLE_ADMIN, 'Admin'),
    (USER_ROLE_STAFF, 'Staff'),
    (USER_ROLE_DRIVER, 'Driver'),
    (USER_ROLE_ESCORT, 'Escort'),
    (USER_ROLE_CUSTOMER, 'Customer')
)

# user document type choices
USER_DOCUMENT_TYPE_D1 = '1'
USER_DOCUMENT_TYPE_D2 = '2'
USER_DOCUMENT_TYPE = (
    (USER_DOCUMENT_TYPE_D1, 'D1'),
    (USER_DOCUMENT_TYPE_D2, 'D2')
)


# Order app - Order status constants
# ----------------------------------------------------------------------------
# order status choices
ORDER_STATUS_PENDING = 'P'
ORDER_STATUS_INPROGRESS = 'I'
ORDER_STATUS_COMPLETE = 'C'
ORDER_STATUS = (
    (ORDER_STATUS_PENDING, 'Pending'),
    (ORDER_STATUS_INPROGRESS, 'In Progress'),
    (ORDER_STATUS_COMPLETE, 'Complete')
)

# order source choices
ORDER_SOURCE_INTERNAL = 'I'
ORDER_SOURCE_CUSTOMER = 'C'
ORDER_SOURCE = (
    (ORDER_SOURCE_INTERNAL, 'From Staff'),
    (ORDER_SOURCE_CUSTOMER, 'From Customer')
)


# job app
# ----------------------------------------------------------------------------
# job status choices
JOB_PROGRESS_NOT_STARTED = 'NT'
JOB_PROGRESS_STARTED = 'ST'
JOB_PROGRESS_TO_LOADNG_STATION = 'TL'
JOB_PROGRESS_ARRIVED_AT_LOADING_STATION = 'AL'
JOB_PROGRESS_DEPARTURE_LOADING_STATION = 'DL'
JOB_PROGRESS_TO_UNLOADING_STATION = 'TU'
JOB_PROGRESS_ARRIVED_AT_UNLOADING_STATION = 'AU'
JOB_PROGRESS_COMPLETE = 'C'

JOB_PROGRESS = (
    (JOB_PROGRESS_NOT_STARTED, 'Not Started'),
    (JOB_PROGRESS_STARTED, 'Started'),
    (JOB_PROGRESS_TO_LOADNG_STATION, 'To Loading Station'),
    (JOB_PROGRESS_ARRIVED_AT_LOADING_STATION, 'Arrived at Loading Station'),
    (JOB_PROGRESS_DEPARTURE_LOADING_STATION, 'Departure at Loading Station'),
    (JOB_PROGRESS_TO_UNLOADING_STATION, 'To UnLoading Station'),
    (JOB_PROGRESS_ARRIVED_AT_UNLOADING_STATION, 'Arrived at Unloading Station'),
    (JOB_PROGRESS_COMPLETE, 'Complete')
)


# road app
# ----------------------------------------------------------------------------
BLACKDOT_TYPE_ROAD_REPAIR = 'R'
BLACKDOT_TYPE_ROAD_LIMIT_TIME = 'L'
BLACKDOT_TYPE = (
    (BLACKDOT_TYPE_ROAD_REPAIR, 'Repair Road'),
    (BLACKDOT_TYPE_ROAD_LIMIT_TIME, 'Time Limit')
)

# Metric Units constants
# ----------------------------------------------------------------------------
UNIT_WEIGHT_TON = 'T'
UNIT_WEIGHT_KILOGRAM = 'K'
UNIT_WEIGHT = (
    (UNIT_WEIGHT_TON, 't'),
    (UNIT_WEIGHT_KILOGRAM, 'Kg')
)

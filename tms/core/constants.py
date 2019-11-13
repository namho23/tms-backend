# Info app
# ----------------------------------------------------------------------------
# station type
STATION_TYPE_LOADING_STATION = 0
STATION_TYPE_QUALITY_STATION = 1
STATION_TYPE_UNLOADING_STATION = 2
STATION_TYPE_OIL_STATION = 3
STATION_TYPE_GET_OFF_STATION = 4
STATION_TYPE_BLACK_DOT = 5
STATION_TYPE_PARKING_STATION = 6
STATION_TYPE_REPAIR_STATION = 7
STATION_TYPE_CUSTOM_POINT = 8
STATION_TYPE = (
    (STATION_TYPE_LOADING_STATION, '装货地'),
    (STATION_TYPE_QUALITY_STATION, '质检点'),
    (STATION_TYPE_UNLOADING_STATION, '卸货地'),
    (STATION_TYPE_OIL_STATION, '合作油站'),
    (STATION_TYPE_GET_OFF_STATION, '下车地管理'),
    (STATION_TYPE_BLACK_DOT, '黑点'),
    (STATION_TYPE_PARKING_STATION, '合法停车区域'),
    (STATION_TYPE_REPAIR_STATION, '供应商'),
    (STATION_TYPE_CUSTOM_POINT, '自定义'),
)

# duration unit choices
TIME_MEASURE_UNIT_MINITE = 'M'
TIME_MEASURE_UNIT_HOUR = 'H'
TIME_MEASURE_UNIT = (
    (TIME_MEASURE_UNIT_MINITE, '分钟'),
    (TIME_MEASURE_UNIT_HOUR, '小时'),
)

PRICE_VARY_DURATION_UNIT_WEEK = 'W'
PRICE_VARY_DURATION_UNIT_MONTH = 'M'
PRICE_VARY_DURATION_UNIT_YEAR = 'Y'
PRICE_VARY_DURATION_UNIT = (
    (PRICE_VARY_DURATION_UNIT_WEEK, '周'),
    (PRICE_VARY_DURATION_UNIT_MONTH, '月'),
    (PRICE_VARY_DURATION_UNIT_YEAR, '年')
)

# product unit measure choices
PRODUCT_WEIGHT_MEASURE_UNIT_LITRE = 'L'
PRODUCT_WEIGHT_MEASURE_UNIT_TON = 'T'
PRODUCT_WEIGHT_MEASURE_UNIT = (
    (PRODUCT_WEIGHT_MEASURE_UNIT_LITRE, '公升'),
    (PRODUCT_WEIGHT_MEASURE_UNIT_TON, '吨')
)

DOCUMENT_EXPIRES_NOTIFICATION_DURATION_DAY = 'D'
DOCUMENT_EXPIRES_NOTIFICATION_DURATION_MONTH = 'M'
DOCUMENT_EXPIRES_NOTIFICATION_DURATION = (
    (DOCUMENT_EXPIRES_NOTIFICATION_DURATION_DAY, '日'),
    (DOCUMENT_EXPIRES_NOTIFICATION_DURATION_MONTH, '月'),
)


# Vehicle app - Vehicle constants
# ----------------------------------------------------------------------------
# vehicle model choices
VEHICLE_MODEL_TYPE_TRUCK = 'T'
VEHICLE_MODEL_TYPE_SEMI_TRAILER = 'S'
VEHICLE_MODEL_TYPE = (
    (VEHICLE_MODEL_TYPE_TRUCK, '牵引车'),
    (VEHICLE_MODEL_TYPE_SEMI_TRAILER, '半挂罐车')
)

VEHICLE_VIOLATION_STATUS_PENDING = 0
VEHICLE_VIOLATION_STATUS_PROCESSED = 1
VEHICLE_VIOLATION_STATUS = (
    (VEHICLE_VIOLATION_STATUS_PENDING, '未处理'),
    (VEHICLE_VIOLATION_STATUS_PROCESSED, '已处理'),
)


# vehicle brand choices
VEHICLE_BRAND_TONGHUA = 'T'
VEHICLE_BRAND_LIBERATION = 'L'
VEHICLE_BRAND_YANGZHOU = 'Y'
VEHICLE_BRAND = (
    (VEHICLE_BRAND_TONGHUA, '通华'),
    (VEHICLE_BRAND_LIBERATION, '解放'),
    (VEHICLE_BRAND_YANGZHOU, '扬州中集')
)

# vehicle document type choices
VEHICLE_DOCUMENT_TYPE_D1 = '1'
VEHICLE_DOCUMENT_TYPE_D2 = '2'
VEHICLE_DOCUMENT_TYPE = (
    (VEHICLE_DOCUMENT_TYPE_D1, 'D1'),
    (VEHICLE_DOCUMENT_TYPE_D2, 'D2')
)

# vehicle status
VEHICLE_STATUS_AVAILABLE = 0
VEHICLE_STATUS_DRIVER_ON = 1
VEHICLE_STATUS_ESCORT_ON = 2
VEHICLE_STATUS_UNDER_WHEEL = 3
VEHICLE_STATUS_REPAIR = 4
VEHICLE_STATUS = (
    (VEHICLE_STATUS_AVAILABLE, 'Available'),
    (VEHICLE_STATUS_DRIVER_ON, 'Driver on'),
    (VEHICLE_STATUS_ESCORT_ON, 'Escort on'),
    (VEHICLE_STATUS_UNDER_WHEEL, 'Under wheel'),
    (VEHICLE_STATUS_REPAIR, 'Repair')
)

# vehicle maintenace type
VEHICLE_MAINTENANCE_CATEGORY_WHEEL = 0
VEHICLE_MAINTENANCE_CATEGORY_OIL_ENGINE = 1
VEHICLE_MAINTENANCE_CATEGORY = (
    (VEHICLE_MAINTENANCE_CATEGORY_WHEEL, '驱动轮'),
    (VEHICLE_MAINTENANCE_CATEGORY_OIL_ENGINE, '齿轮油'),
)

VEHICLE_USER_BIND_METHOD_BY_ADMIN = 'A'
VEHICLE_USER_BIND_METHOD_BY_JOB = 'J'
VEHICLE_USER_BIND_METHOD = (
    (VEHICLE_USER_BIND_METHOD_BY_ADMIN, 'By Admin'),
    (VEHICLE_USER_BIND_METHOD_BY_JOB, 'By Job')
)

VEHICLE_CHECK_TYPE_BEFORE_DRIVING = 'B'
VEHICLE_CHECK_TYPE_DRIVING = 'D'
VEHICLE_CHECK_TYPE_AFTER_DRIVING = 'A'
VEHICLE_CHECK_TYPE = (
    (VEHICLE_CHECK_TYPE_BEFORE_DRIVING, '行车前'),
    (VEHICLE_CHECK_TYPE_DRIVING, '行车中'),
    (VEHICLE_CHECK_TYPE_AFTER_DRIVING, '行车后')
)


# Account app - Account constants
# ----------------------------------------------------------------------------
# user type choices
USER_TYPE_ADMIN = 'A'
USER_TYPE_STAFF = 'S'
USER_TYPE_DRIVER = 'D'
USER_TYPE_ESCORT = 'E'
USER_TYPE_GUEST_DRIVER = 'P'
USER_TYPE_GUEST_ESCORT = 'G'
USER_TYPE_CUSTOMER = 'C'
USER_TYPE_SECURITY_OFFICER = 'T'

USER_TYPE = (
    (USER_TYPE_ADMIN, '管理人员'),
    (USER_TYPE_STAFF, '工作人员'),
    (USER_TYPE_DRIVER, '驾驶人员'),
    (USER_TYPE_ESCORT, '押运人员'),
    (USER_TYPE_GUEST_DRIVER, '外驾驶人员'),
    (USER_TYPE_GUEST_ESCORT, '外押运人员'),
    (USER_TYPE_CUSTOMER, '客户'),
    (USER_TYPE_SECURITY_OFFICER, '检查')
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
    (ORDER_STATUS_PENDING, '未开始'),
    (ORDER_STATUS_INPROGRESS, '已开始'),
    (ORDER_STATUS_COMPLETE, '已完成')
)

TRUCK_ARRANGEMENT_STATUS_PENDING = 'P'
TRUCK_ARRANGEMENT_STATUS_INPROGRESS = 'I'
TRUCK_ARRANGEMENT_STATUS_COMPLETE = 'C'
TRUCK_ARRANGEMENT_STATUS = (
    (TRUCK_ARRANGEMENT_STATUS_PENDING, '未派车'),
    (TRUCK_ARRANGEMENT_STATUS_INPROGRESS, '派车中'),
    (TRUCK_ARRANGEMENT_STATUS_COMPLETE, '派车完')
)
# order source choices
ORDER_SOURCE_INTERNAL = 'I'
ORDER_SOURCE_CUSTOMER = 'C'
ORDER_SOURCE = (
    (ORDER_SOURCE_INTERNAL, '内部'),
    (ORDER_SOURCE_CUSTOMER, 'App')
)

# payment method choices
PAYMENT_METHOD_TON = 'T'
PAYMENT_METHOD_TON_PER_DISTANCE = 'D'
PAYMENT_METHOD_PRICE = 'P'
PAYMENT_METHOD = (
    (PAYMENT_METHOD_TON, '吨'),
    (PAYMENT_METHOD_TON_PER_DISTANCE, '吨/公里'),
    (PAYMENT_METHOD_PRICE, '一口价')
)

ORDER_PAYMENT_STATUS_NO_DISTANCE = 0
ORDER_PAYMENT_STATUS_WAITING_DUIZHANG = 1
ORDER_PAYMENT_STATUS_WAITING_TICKET = 2
ORDER_PAYMENT_STATUS_WAITING_PAYMENT_CONFRIM = 3
ORDER_PAYMENT_STATUS_COMPLETE = 4
ORDER_PAYMENT_STATUS = (
    (ORDER_PAYMENT_STATUS_NO_DISTANCE, '待更新'),
    (ORDER_PAYMENT_STATUS_WAITING_DUIZHANG, '待对账'),
    (ORDER_PAYMENT_STATUS_WAITING_TICKET, '待开票'),
    (ORDER_PAYMENT_STATUS_WAITING_PAYMENT_CONFRIM, '待结算'),
    (ORDER_PAYMENT_STATUS_COMPLETE, '结算'),
)


# job app
# ----------------------------------------------------------------------------
# job status choices
JOB_PROGRESS_COMPLETE = 0
JOB_PROGRESS_NOT_STARTED = 1
JOB_PROGRESS_TO_LOADING_STATION = 2
JOB_PROGRESS_ARRIVED_AT_LOADING_STATION = 3
JOB_PROGRESS_LOADING_AT_LOADING_STATION = 4
JOB_PROGRESS_FINISH_LOADING_AT_LOADING_STATION = 5
JOB_PROGRESS_TO_QUALITY_STATION = 6
JOB_PROGRESS_ARRIVED_AT_QUALITY_STATION = 7
JOB_PROGRESS_CHECKING_AT_QUALITY_STATION = 8
JOB_PROGRESS_FINISH_CHECKING_AT_QUALITY_STATION = 9
JOB_PROGRESS_TO_UNLOADING_STATION = 10
JOB_PRGORESS_ARRIVED_AT_UNLOADING_STATION = 11
JOB_PROGRESS_UNLOADING_AT_UNLOADING_STATION = 12
JOB_PROGRESS_FINISH_UNLOADING_AT_UNLOADING_STATION = 13
JOB_PROGRESS = {
    JOB_PROGRESS_COMPLETE: '已完成',
    JOB_PROGRESS_NOT_STARTED: '未开始',
    JOB_PROGRESS_TO_LOADING_STATION: '赶往装货地',
    JOB_PROGRESS_ARRIVED_AT_LOADING_STATION: '等待装货',
    JOB_PROGRESS_LOADING_AT_LOADING_STATION: '装货中',
    JOB_PROGRESS_FINISH_LOADING_AT_LOADING_STATION: '装货完成',
    JOB_PROGRESS_TO_QUALITY_STATION: '赶往质检',
    JOB_PROGRESS_ARRIVED_AT_QUALITY_STATION: '等待质检',
    JOB_PROGRESS_CHECKING_AT_QUALITY_STATION: '质检中',
    JOB_PROGRESS_FINISH_CHECKING_AT_QUALITY_STATION: '质检完成',
    JOB_PROGRESS_TO_UNLOADING_STATION: '赶往卸货',
    JOB_PRGORESS_ARRIVED_AT_UNLOADING_STATION: '等待卸货',
    JOB_PROGRESS_UNLOADING_AT_UNLOADING_STATION: '卸货中',
    JOB_PROGRESS_FINISH_UNLOADING_AT_UNLOADING_STATION: '卸货完成',
}

# road app
# ----------------------------------------------------------------------------
ROUTE_PLANNING_POLICY_LEAST_TIME = 0
ROUTE_PLANNING_POLICY_LEAST_FEE = 1
ROUTE_PLANNING_POLICY_LEAST_DISTANCE = 2
ROUTE_PLANNING_POLICY = (
    (ROUTE_PLANNING_POLICY_LEAST_TIME, '最快捷模式'),
    (ROUTE_PLANNING_POLICY_LEAST_FEE, '最经济模式'),
    (ROUTE_PLANNING_POLICY_LEAST_DISTANCE, '最短距离模式')
)

# hr app
# ----------------------------------------------------------------------------
PERMISSION_TYPE_NO = 0
PERMISSION_TYPE_READ = 1
PERMISSION_TYPE_WRITE = 2
PERMISSION_TYPE = (
    (PERMISSION_TYPE_NO, 'No permission'),
    (PERMISSION_TYPE_READ, 'Read Permission'),
    (PERMISSION_TYPE_WRITE, 'Write Permission')
)

# business app
# ----------------------------------------------------------------------------
REQUEST_TYPE_REST = 0
REQUEST_TYPE_VEHICLE_REPAIR = 1
REQUEST_TYPE_SELF_DRIVING_PAYMENT = 2
REQUEST_TYPE_INVOICE_PAYMENT = 3
REQUEST_TYPE = (
    (REQUEST_TYPE_REST, '假期'),
    (REQUEST_TYPE_VEHICLE_REPAIR, '车辆修理'),
    (REQUEST_TYPE_SELF_DRIVING_PAYMENT, '自驾车补贴'),
    (REQUEST_TYPE_INVOICE_PAYMENT, '费用报销'),
)

REST_REQUEST_ILL = 'I'
REST_REQUEST_PERSONAL = 'P'
REST_REQUEST_CATEGORY = (
    (REST_REQUEST_ILL, '病假'),
    (REST_REQUEST_PERSONAL, '私事'),
)

APPROVER_TYPE_POSITION = 'P'
APPROVER_TYPE_MEMBER = 'W'
APPROVER_TYPE = (
    (APPROVER_TYPE_POSITION, '职位'),
    (APPROVER_TYPE_MEMBER, '人员'),
)

CC_TYPE_POSITION = 'P'
CC_TYPE_MEMBER = 'W'
CC_TYPE = (
    (CC_TYPE_POSITION, '职位'),
    (CC_TYPE_MEMBER, '人员'),
)

VEHICLE_REPAIR_REQUEST_CATEGORY_BRAKE = 'B'
VEHICLE_REPAIR_REQUEST_CATEGORY = (
    (VEHICLE_REPAIR_REQUEST_CATEGORY_BRAKE, '查看刹车'),
)


# notification app
# ----------------------------------------------------------------------------
# event type
EVENT_TYPE_DRIVER_LICENSE_EXPIRED = 0
EVENT_TYPE_VEHICLE_LICENSE_EXPIRED = 1
EVENT_TYPE_VEHICLE_OPERATION_PERMIT_EXPIRED = 2
EVENT_TYPE_VEHICLE_INSURANCE_EXPIRED = 3
EVENT_TYPE = (
    (EVENT_TYPE_DRIVER_LICENSE_EXPIRED, '驾驶证'),
    (EVENT_TYPE_VEHICLE_LICENSE_EXPIRED, '车辆行驶证'),
    (EVENT_TYPE_VEHICLE_OPERATION_PERMIT_EXPIRED, '车辆运营证'),
    (EVENT_TYPE_VEHICLE_INSURANCE_EXPIRED, '车辆保险'),
)

# driver status
WORK_STATUS_AVAILABLE = 0
WORK_STATUS_DRIVING = 1
WORK_STATUS_NOT_AVAILABLE = 2
WORK_STATUS = (
    (WORK_STATUS_AVAILABLE, 'Available'),
    (WORK_STATUS_DRIVING, 'Driving'),
    (WORK_STATUS_NOT_AVAILABLE, 'Not Available')
)

# driver notification
DRIVER_NOTIFICATION_NEW_JOB = 0
DRIVER_NOTIFICATION_UPDATE_JOB = 1
DRIVER_NOTIFICATION_DELETE_JOB = 2
DRIVER_NOTIFICATION_CANCEL_JOB = 3
DRIVER_NOTIFICATION_TYPE_ENTER_STATION = 4
DRIVER_NOTIFICATION_TYPE_EXIT_STATION = 5
DRIVER_NOTIFICATION_TYPE_ENTER_BLACK_DOT = 6
DRIVER_NOTIFICATION_TYPE_EXIT_BLACK_DOT = 7
DRIVER_NOTIFICATION_TYPE_CHANGE_WORKER = 8
DRIVER_NOTIFICATION_PROGRESS_SYNC = 9
# reserved 7-9


# customer notification
CUSTOMER_NOTIFICATION_NEW_ORDER = 70
CUSTOMER_NOTIFICATION_UPDATE_ORDER = 73
CUSTOMER_NOTIFICATION_DELETE_ORDER = 74
CUSTOMER_NOTIFICATION_NEW_ARRANGEMENT = 71
CUSTOMER_NOTIFICATION_UPDATE_ARRANGEMENT = 72

# staff notification
NOTIFICATION_REST_REQUEST = 10
NOTIFICATION_REST_REQUEST_APPROVED = 11
NOTIFICATION_REST_REQUEST_DECLINED = 12

NOTIFICATION_VEHICLE_REPAIR_REQUEST = 20
NOTIFICATION_VEHICLE_REPAIR_REQUEST_APPROVED = 21
NOTIFICATION_VEHICLE_REPAIR_REQUEST_DECLINED = 22

NOTIFICATION_PARKING_REQUEST = 30
NOTIFICATION_PARKING_REQUEST_APPROVED = 31
NOTIFICATION_PARKING_REQUEST_DECLINED = 32

NOTIFICATION_DRIVER_CHANGE_REQUEST = 40
NOTIFICATION_DRIVER_CHANGE_REQUEST_APPROVED = 41
NOTIFICATION_DRIVER_CHANGE_REQUEST_DECLINED = 42
NOTIFICATION_DRIVER_CHANGE_REQUEST_NEW_DRIVER = 43

NOTIFICATION_ESCORT_CHANGE_REQUEST = 50
NOTIFICATION_ESCORT_CHANGE_REQUEST_APPROVED = 51
NOTIFICATION_ESCORT_CHANGE_REQUEST_DECLINED = 52
NOTIFICATION_ESCORT_CHANGE_REQUEST_NEW_ESCORT = 53

NOTIFICATION_TRAFFIC_ACCIDENT = 60

NOTIFICATION_TYPE = (
    # driver app
    (DRIVER_NOTIFICATION_NEW_JOB, 'New Job'),
    (DRIVER_NOTIFICATION_UPDATE_JOB, 'Update Job'),
    (DRIVER_NOTIFICATION_DELETE_JOB, 'Delete Job'),
    (DRIVER_NOTIFICATION_CANCEL_JOB, 'Cancel Job'),
    (DRIVER_NOTIFICATION_TYPE_ENTER_STATION, 'Enter station'),
    (DRIVER_NOTIFICATION_TYPE_EXIT_STATION, 'Exit Station'),
    (DRIVER_NOTIFICATION_TYPE_ENTER_BLACK_DOT, 'Enter Blackdot'),
    (DRIVER_NOTIFICATION_TYPE_EXIT_BLACK_DOT, 'Exit Blackdot'),
    (DRIVER_NOTIFICATION_TYPE_CHANGE_WORKER, 'Change worker'),

    # Customer app
    (CUSTOMER_NOTIFICATION_NEW_ORDER, 'New Order'),
    (CUSTOMER_NOTIFICATION_UPDATE_ORDER, 'Update Order'),
    (CUSTOMER_NOTIFICATION_DELETE_ORDER, 'Delete Order'),
    (CUSTOMER_NOTIFICATION_NEW_ARRANGEMENT, 'New Arrangement'),
    (CUSTOMER_NOTIFICATION_UPDATE_ARRANGEMENT, 'Update Arrangement'),

    (NOTIFICATION_REST_REQUEST,
        'Rest Request Notification'),
    (NOTIFICATION_REST_REQUEST_APPROVED,
        'Rest Request Notification Approved'),
    (NOTIFICATION_REST_REQUEST_DECLINED,
        'Rest Request Notification Declined'),
    (NOTIFICATION_VEHICLE_REPAIR_REQUEST,
        'Vehicle Maintenance Notification'),
    (NOTIFICATION_VEHICLE_REPAIR_REQUEST_APPROVED,
        'Vehicle Maintenance Notification Approved'),
    (NOTIFICATION_VEHICLE_REPAIR_REQUEST_DECLINED,
        'Vehicle Maintenance Notification Declined'),
    (NOTIFICATION_PARKING_REQUEST,
        'Parking Request Notification'),
    (NOTIFICATION_PARKING_REQUEST_APPROVED,
        'Parking Request Notification Approved'),
    (NOTIFICATION_PARKING_REQUEST_DECLINED,
        'Parking Request Notification Declined'),
    (NOTIFICATION_DRIVER_CHANGE_REQUEST,
        'Driver Change Notification'),
    (NOTIFICATION_DRIVER_CHANGE_REQUEST_APPROVED,
        'Driver Change Notification Approved'),
    (NOTIFICATION_DRIVER_CHANGE_REQUEST_DECLINED,
        'Driver Change Notification Declined'),
    (NOTIFICATION_DRIVER_CHANGE_REQUEST_NEW_DRIVER,
        'Driver Change Notification New Driver'),
    (NOTIFICATION_ESCORT_CHANGE_REQUEST,
        'Escort Change Notification'),
    (NOTIFICATION_ESCORT_CHANGE_REQUEST_APPROVED,
        'Escort Change Notification Approved'),
    (NOTIFICATION_ESCORT_CHANGE_REQUEST_DECLINED,
        'Escort Change Notification Declined'),
    (NOTIFICATION_ESCORT_CHANGE_REQUEST_NEW_ESCORT,
        'Escort Change Notification New Escort'),
    (NOTIFICATION_TRAFFIC_ACCIDENT,
        'Traffic Accident Notification'),
)


# finance app
# ----------------------------------------------------------------------------
# bill document type
BILL_CATEGORY_MEAL = 0
BILL_CATEGORY_PARKING_VEHICLE = 1
BILL_CATEGORY_CLEAN_VEHICLE = 2
BILL_CATEGORY_SLEEP = 3
BILL_FROM_OIL_STATION = 4
BILL_CATEGORY = (
    (BILL_CATEGORY_MEAL, '吃饭'),
    (BILL_CATEGORY_PARKING_VEHICLE, '停车'),
    (BILL_CATEGORY_CLEAN_VEHICLE, '洗车'),
    (BILL_CATEGORY_SLEEP, '住宿')
)

OIL_BILL_BY_CARD = 0
OIL_BILL_BY_CASH = 1
OIL_BILL_BY_OTHER = 2
OIL_BILL_SUB_CATEGORY = (
    (OIL_BILL_BY_CARD, '油卡加油'),
    (OIL_BILL_BY_CASH, '现金加油'),
    (OIL_BILL_BY_OTHER, '小贾加油')
)

TRAFFIC_BILL_BY_CARD = 0
TRAFFIC_BILL_BY__WITHOUT_TICKET = 1
TRAFFIC_BILL_BY_CASH = 2
TRAFFIC_BILL_SUB_CATEGORY = (
    (TRAFFIC_BILL_BY_CARD, '鲁通卡刷卡'),
    (TRAFFIC_BILL_BY__WITHOUT_TICKET, '鲁通卡无票'),
    (TRAFFIC_BILL_BY_CASH, '路票现金')
)

PARKING_BILL = 0
WASH_BILL = 1
TOLL_FEE = 2
TRAFFIC_VIOLATION_BILL = 3
TRUCK_REPAIR_BILL = 4
MEAL_BILL = 5
STAY_BILL = 6
EXTRA_BILL = 7
OTHER_BILL_SUB_CATEGORY = (
    (PARKING_BILL, '停车场'),
    (WASH_BILL, '洗车费'),
    (TOLL_FEE, '带路费'),
    (TRAFFIC_VIOLATION_BILL, '违章费'),
    (TRUCK_REPAIR_BILL, '修车费'),
    (MEAL_BILL, '吃饭'),
    (STAY_BILL, '睡觉'),
    (EXTRA_BILL, '更多'),
)

TRAFFIC_VIOLATION_RED_LIGHT = 0
TRAFFIC_VIOLATION_TRUCK_LINE = 1
TRAFFIC_VIOLATION_OVER_SPEED = 2
TRAFFIC_VIOLATION_OVER_WEIGHT = 3
TRAFFIC_VIOLATION_DETAIL_CATEGORY = (
    (TRAFFIC_VIOLATION_RED_LIGHT, '闯红灯'),
    (TRAFFIC_VIOLATION_TRUCK_LINE, '不安导向车道行驶'),
    (TRAFFIC_VIOLATION_OVER_SPEED, '超速'),
    (TRAFFIC_VIOLATION_OVER_WEIGHT, '超重'),
)


# warehouse app
# ----------------------------------------------------------------------------
WEIGHT_UNIT_KG = 'K'
WEIGHT_UNIT_TON = 'T'
WEIGHT_UNIT = (
    (WEIGHT_UNIT_KG, '公斤'),
    (WEIGHT_UNIT_TON, '吨')
)


# security app
# ----------------------------------------------------------------------------
COMPANY_POLICY_TYPE_SHELL = 'S'
COMPANY_POLICY_TYPE_TRANSPORTATION = 'T'
COMPANY_POLICY_TYPE_OIL = 'O'
COMPANY_POLICY_TYPE_ALL = 'A'
COMPANY_POLICY_TYPE = (
    (COMPANY_POLICY_TYPE_SHELL, '壳牌'),
    (COMPANY_POLICY_TYPE_TRANSPORTATION, '危化品运输部'),
    (COMPANY_POLICY_TYPE_OIL, '油品'),
    (COMPANY_POLICY_TYPE_ALL, '全部')
)

QUESTION_TYPE_BOOLEN = 0
QUESTION_TYPE_SINGLE_CHOICE = 1
QUESTION_TYPE_MULTIPLE_CHOICE = 2
QUESTION_TYPE = (
    (QUESTION_TYPE_BOOLEN, '判断题'),
    (QUESTION_TYPE_SINGLE_CHOICE, '单选题'),
    (QUESTION_TYPE_MULTIPLE_CHOICE, '多选题'),
)

WORKER_TYPE_DRIVER = 'D'
WORKER_TYPE_ESCORT = 'E'
WORKER_TYPE = (
    (WORKER_TYPE_DRIVER, '司机'),
    (WORKER_TYPE_ESCORT, '押运员'),
)


EXCEL_BODY_STYLE = {
    'height': 25,
    'style': {
        'alignment': {
            'horizontal': 'center',
            'vertical': 'center',
            'wrapText': True,
            'shrink_to_fit': True,
        },
        'border_side': {
            'border_style': 'thin',
            'color': 'FF000000',
        },
        'font': {
            'name': 'Arial',
            'size': 14,
            'bold': False,
            'color': 'FF000000',
        }
    }
}

EXCEL_HEAD_STYLE = {
    'height': 40,
    'style': {
        'fill': {
            'fill_type': 'solid',
            'start_color': 'FFCCFFCC',
        },
        'alignment': {
            'horizontal': 'center',
            'vertical': 'center',
            'wrapText': True,
            'shrink_to_fit': True,
        },
        'border_side': {
            'border_style': 'thin',
            'color': 'FF000000',
        },
        'font': {
            'name': 'Arial',
            'size': 14,
            'bold': True,
            'color': 'FF000000',
        }
    }
}

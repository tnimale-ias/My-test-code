from pyspark.sql import SparkSession, functions, Row, types
from pyspark.sql.functions import from_json, col, lit, concat, window, when, pandas_udf, PandasUDFType, udf
from pyspark.sql.types import StructType, StringType, LongType, DoubleType
from typing import Union





########################################## Anzu Gaming Partner #################################################

# EVENTS
WINDOW_TIME = 30  # in seconds
LOAD_EVENT = 'Load'
IMPRESSION_EVENT = 'Impression'
VIEWABLE_IMPRESSION_EVENT = 'ViewableImpression'
UNLOAD_EVENT = 'Unload'

# FIELDS/SCHEMA
AD_ID = 'adID'
EVENT_TYPE = 'eventType'
EVENT_TIME = 'eventCreationTimestamp'
EVENT_TIME_ZONE = 'eventTimeZone'
EVENT_SESSION_ID = 'eventSessionID'
AD_SESSION_ID = 'adSessionID'
CUMULATIVE_50PCT_INVIEW_DURATION = 'cumulative50PctInviewDuration'
MAX_CONTINUOUS_50PCT_INVIEW_DURATION = 'maxCumulative50PctInviewDuration'
CUMULATIVE_100PCT_INVIEW_DURATION = 'cumulative100PctInviewDuration'
MAX_CONTINUOUS_100PCT_INVIEW_DURATION = 'maxCumulative100PctInviewDuration'
DWELL_DURATION = 'dwellDuration'
AVG_PCT_SEEN_WHILE_ON_SCREEN = 'avgPctSeenWhileOnScreen'
MAX_PCT_SEEN_WHILE_ON_SCREEN = 'maxPctSeenWhileOnScreen'
MIN_PCT_SEEN_WHILE_ON_SCREEN = 'minPctSeenWhileOnScreen'
AVERAGE_ON_SCREEN_REAL_ESTATE = 'avgOnScreenRealEstate'
MAX_ON_SCREEN_REAL_ESTATE = 'maxOnScreenRealEstate'
MIN_ON_SCREEN_REAL_ESTATE = 'maxOnScreenRealEstate'
AVERAGE_ANGLE_WHILE_ON_SCREEN = 'avgAngleWhileOnScreen'
AVG_ANGLE_DURATION = 'avgAngleDuration'
MAX_ANGLE_WHILE_ON_SCREEN = 'maxAngleWhileOnScreen'
MAX_ANGLE_DURATION = 'maxAngleDuration'
MIN_ANGLE_WHILE_ON_SCREEN = 'minAngleWhileOnScreen'
MIN_ANGLE_DURATION = 'minAngleDuration'
PROGRESS = 'progress'
DEVICE_MODEL = 'deviceModel'
DEVICE_MANUFACTURER = 'deviceManufacturer'
OS = 'os'
OS_VERSION = 'osVersion'
SDK_NAME = 'sdkName'
SDK_VERSION = 'sdkVersion'
BID_ID = 'bidID'
ADVERTISER_DOMAIN = 'advertiserDomain'
AD_UNIT_TYPE = 'adUnitType'
START_TIMESTAMP = 'startTimestamp'
CACHE_BUSTER = 'cacheBuster'
APP_STORE_NAME = 'appStoreName'
APP_STORE_ID = 'appStoreID'
PLACEMENT_ID = 'placementID'
ORDER_ID = 'orderID'
LINE_ITEM_ID = 'lineItemID'
CREATIVE_ID = 'creativeID'
AD_HEIGHT = 'adHeight'
AD_WIDTH = 'adWidth'
SCREEN_WIDTH = 'screenWidth'
SCREEN_HEIGHT = 'screenHeight'
GAME_NAME = 'gameName'
AD_NETWORK_ID = 'adNetworkID'
ADVERTISER_ID = 'advertiserID'
ADVERTISER_NAME = 'advertiserName'
CAMPAIGN_ID = 'campaignID'
EXT_CAMPAIGN_ID = 'extCampaignID'
PUBLISHER_ID = 'pub_id'
PUBLISHER_NAME = 'publisherName'
COUNTRY_CODE = 'countryCode'
STATE_CODE = 'stateCode'
DMA = 'dma'
UID = 'uid'
IMPRESSION_ID = 'impID'
BUNDLE_ID = 'bundleID'
AD_SERVER_NAME = 'adServerName'
MEDIA_TYPE = 'mediaType'
VIDEO_PLAYER_STATE = 'videoPlayerState'
VIDEO_BREAK_POSITION = 'videoBreakPosition'
AUTO_REFRESH_ENABLE = 'autoRefreshEnable'



spark = SparkSession.builder.appName("Merging events test").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

def read_topic(topic):
    df = spark.readStream.format("kafka") \
        .option("kafka.bootstrap.servers", "b-3.gamingmskprodmskcluste.g1qnir.c3.kafka.us-east-1.amazonaws.com:9092,b-2.gamingmskprodmskcluste.g1qnir.c3.kafka.us-east-1.amazonaws.com:9092,b-1.gamingmskprodmskcluste.g1qnir.c3.kafka.us-east-1.amazonaws.com:9092") \
        .option("subscribe",topic) \
        .option('failOnDataLoss', 'false') \
        .load()\
        .withColumn("current_timestamp", functions.unix_timestamp())

    df.printSchema()
    return df


def get_merge_schema():
    schema = StructType().add(AD_ID, StringType()) \
        .add(EVENT_TYPE, StringType()) \
        .add(EVENT_TIME, LongType()) \
        .add(MEDIA_TYPE, StringType()) \
        .add(AVERAGE_ANGLE_WHILE_ON_SCREEN, DoubleType()) \
        .add(AVERAGE_ON_SCREEN_REAL_ESTATE, DoubleType()) \
        .add(MAX_ON_SCREEN_REAL_ESTATE, DoubleType())
    return schema


def get_final_event(df):

    event = df.selectExpr("CAST(value AS STRING)")
    event_schema = get_merge_schema()
    stream_event = event.select(from_json(col("value"), event_schema).alias("event_details"))
    print(stream_event)
    final_event = stream_event.select("event_details.*").withColumn("current_timeStamp", functions.current_timestamp())
    return final_event




def check_events(events: list):

    if UNLOAD_EVENT in events:
        if LOAD_EVENT in events:
            if IMPRESSION_EVENT in events:
                if VIEWABLE_IMPRESSION_EVENT in events:
                    return 'load_impression_viewable_impression_unload_event_present'
                else:
                    return 'load_impression_unload_event_present_unmeasured'
            else:
                if VIEWABLE_IMPRESSION_EVENT in events:
                    return 'load_viewable_impression_unload_event_present'
                else:
                    return 'load_unload_event_present_unmeasured'
        else:
            if IMPRESSION_EVENT in events:
                if VIEWABLE_IMPRESSION_EVENT in events:
                    return 'impression_viewable_impression_unload_event_present'
                else:
                    return 'impression_unload_event_present_unmeasured'
            else:
                if VIEWABLE_IMPRESSION_EVENT in events:
                    return 'viewable_impression_unload_event_present'
                else:
                    return 'unload_event_present_unmeasured'

    else:
        if LOAD_EVENT in events:
            if IMPRESSION_EVENT in events:
                if VIEWABLE_IMPRESSION_EVENT in events:
                    return 'load_impression_viewable_impression_event_present'
                else:
                    return 'load_impression_event_present_unmeasured'
            else:
                if VIEWABLE_IMPRESSION_EVENT in events:
                    return 'load_viewable_impression_event_present'
                else:
                    return 'load_event_present_unmeasured'

        else:
            if IMPRESSION_EVENT in events:
                if VIEWABLE_IMPRESSION_EVENT in events:
                    return 'impression_viewable_impression_event_present'
                else:
                    return 'impression_event_present_unmeasured'
            else:
                if VIEWABLE_IMPRESSION_EVENT in events:
                    return 'viewable_impression_event_present'
                else:
                    return 'unmeasured'




#Function that returns a string with first character of each eventType indicating the order of events received...
def event_order(events):
    event_order = ''
    for event in events:
        event_order+=event[0].lower()
    return event_order





#Functions that returns the index of element in the list eliminating the values that are null for the list...
#For example evtnType Load as null values in averageViewAngle so there wont be value corresponding to those in the list
#Thus we need to skip those indexes to get the right index of the data
def get_index(list: list, data: Union[int, float, str], ommit_value: Union[int, float, str]):
    offset = 0
    for index, value in enumerate(list):
        if value==ommit_value:
            offset+=1
        if value==data:
            return index-offset
    return -1



#Function that aggregates based on priority order Unload -> Viewable IMpression -> Impression -> Load
def calculate_decendingPriorityDouble(events: list, listValues: list):

    if UNLOAD_EVENT in events:
        return listValues[get_index(events, UNLOAD_EVENT, LOAD_EVENT)]
    elif VIEWABLE_IMPRESSION_EVENT in events:
        #return avgAngleWhileOnScreen[events.index('ViewableImpression')]
        return listValues[get_index(events, VIEWABLE_IMPRESSION_EVENT, LOAD_EVENT)]
    elif IMPRESSION_EVENT in events:
        #return avgAngleWhileOnScreen[events.index('Impression')]
        return listValues[get_index(events, IMPRESSION_EVENT, LOAD_EVENT)]
    else:
        return None




#Define all the UDFs....
check_events_udf = functions.udf(check_events, types.StringType())
event_order_udf = functions.udf(event_order, types.StringType())
calculate_decendingPriorityDouble_udf = functions.udf(calculate_decendingPriorityDouble, types.DoubleType())


df = read_topic("gaming.lld")
final_event = get_final_event(df)

#Aggregate function based on Watermarking and time based sliding window....
new_event = final_event\
        .withWatermark('current_timeStamp', '300 seconds')\
        .groupBy(window('current_timeStamp', '300 seconds', '150 seconds'), AD_ID)\
        .agg(
        functions.count(final_event[EVENT_TYPE]).alias('events'),
        functions.lit('aggregate').alias(EVENT_TYPE),
        event_order_udf(functions.collect_list(EVENT_TYPE)).alias('event_order'),
        check_events_udf(functions.collect_list(EVENT_TYPE)).alias('completion_reason'),
        functions.max(EVENT_TIME).alias(EVENT_TIME),
        functions.max(MEDIA_TYPE).alias(MEDIA_TYPE),
        calculate_decendingPriorityDouble_udf(functions.collect_list(EVENT_TYPE), functions.collect_list(AVERAGE_ANGLE_WHILE_ON_SCREEN)).alias(AVERAGE_ANGLE_WHILE_ON_SCREEN),
        calculate_decendingPriorityDouble_udf(functions.collect_list(EVENT_TYPE), functions.collect_list(AVERAGE_ON_SCREEN_REAL_ESTATE)).alias(AVERAGE_ON_SCREEN_REAL_ESTATE),
        calculate_decendingPriorityDouble_udf(functions.collect_list(EVENT_TYPE), functions.collect_list(MAX_ON_SCREEN_REAL_ESTATE)).alias(MAX_ON_SCREEN_REAL_ESTATE),
        functions.lit('test-value').alias('value'),
        functions.min('current_timeStamp').alias('current_timeStamp'))\



kafka_output = new_event \
    .selectExpr("to_json(struct(*)) AS value")\
    .writeStream \
    .trigger(processingTime='1 seconds') \
    .outputMode("update") \
    .option("truncate", "false") \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "b-3.gamingmskprodmskcluste.g1qnir.c3.kafka.us-east-1.amazonaws.com:9092,b-2.gamingmskprodmskcluste.g1qnir.c3.kafka.us-east-1.amazonaws.com:9092,b-1.gamingmskprodmskcluste.g1qnir.c3.kafka.us-east-1.amazonaws.com:9092") \
    .option("topic", "merge_events") \
    .option("checkpointLocation", "/tmp/test1/checkpoint")\
    .start()


kafka_output.awaitTermination()



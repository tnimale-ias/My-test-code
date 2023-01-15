string = """{
  "event-type": "Load",
  "event-timestamp": 1668490574,
  "media_type": "Banner",
  "ad_id": "ab01"
}
{
  "event-type": "Load",
  "event-timestamp": 1668490574,
  "media_type": "Banner",
  "ad_id": "aa01"
}
{
  "event-type": "Impression",
  "event-timestamp": 1668490579,
  "avg_angle_while_on_screen": 4.981058,
  "avg_on_screen_real_state": 7.665796,
  "max_on_screen_real_state": 20.373024,
  "ad_id": "aa01"
}
{
  "event-type": "Impression",
  "event-timestamp": 1668490583,
  "avg_angle_while_on_screen": 11.0062675,
  "avg_on_screen_real_state": 5.659506,
  "max_on_screen_real_state": 20.1388912,
  "ad_id": "ab01"
}
{
  "event-type": "Unload",
  "event-timestamp": 1668490587,
  "ad_id": "aa01"
}
{
  "event-type": "Load",
  "event-timestamp": 1668490589,
  "media_type": "Banner",
  "ad_id": "ad6"
}
{
  "event-type": "Impression",
  "event-timestamp": 1668490594,
  "avg_angle_while_on_screen": 4.38552475,
  "avg_on_screen_real_state": 5.28346539,
  "max_on_screen_real_state": 16.8178387,
  "ad_id": "ad6"
}
{
  "event-type": "Impression",
  "event-timestamp": 1668490597,
  "avg_angle_while_on_screen": 10.1636477,
  "avg_on_screen_real_state": 5.020199,
  "max_on_screen_real_state": 20.7878571,
  "ad_id": "ab01"
}
{
  "event-type": "Impression",
  "event-timestamp": 1668490604,
  "avg_angle_while_on_screen": 4.50536633,
  "avg_on_screen_real_state": 9.362757,
  "max_on_screen_real_state": 21.2085724,
  "ad_id": "ad6"
}
{
  "event-type": "Unload",
  "event-timestamp": 1668490614,
  "ad_id": "ad6"
}
{
  "event-type": "Load",
  "event-timestamp": 1668490620,
  "media_type": "Banner",
  "ad_id": "ad9"
}
{
  "event-type": "Impression",
  "event-timestamp": 1668490621,
  "avg_angle_while_on_screen": 10.66736,
  "avg_on_screen_real_state": 7.60154,
  "max_on_screen_real_state": 22.483125,
  "ad_id": "ab01"
}
{
  "event-type": "Impression",
  "event-timestamp": 1668490624,
  "avg_angle_while_on_screen": 4.745754,
  "avg_on_screen_real_state": 5.63769,
  "max_on_screen_real_state": 15.9529505,
  "ad_id": "ad9"
}
{
  "event-type": "Impression",
  "event-timestamp": 1668490626,
  "avg_angle_while_on_screen": 9.899589,
  "avg_on_screen_real_state": 7.601169,
  "max_on_screen_real_state": 19.4091244,
  "ad_id": "ab01"
}
{
  "event-type": "Unload",
  "event-timestamp": 1668490632,
  "ad_id": "ad9"
}
{
  "event-type": "Load",
  "event-timestamp": 1668490636,
  "media_type": "Banner",
  "ad_id": "ad11"
}
{
  "event-type": "Impression",
  "event-timestamp": 1668490637,
  "avg_angle_while_on_screen": 3.35981035,
  "avg_on_screen_real_state": 4.52192259,
  "max_on_screen_real_state": 17.5390854,
  "ad_id": "ad11"
}
{
  "event-type": "Unload",
  "event-timestamp": 1668490645,
  "ad_id": "ad11"
}

{
  "event-type": "Unload",
  "event-timestamp": 1668490647,
  "ad_id": "ab01"
}"""

print('event-type' in string)

string = string.replace('event-type', 'eventType')
string = string.replace('event-timestamp', 'eventCreationTimestamp')
string = string.replace('ad_id', 'adID')
string = string.replace('avg_angle_while_on_screen', 'avgAngleWhileOnScreen')
string = string.replace('avg_on_screen_real_state', 'avgOnScreenRealEstate')
string = string.replace('max_on_screen_real_state', 'maxOnScreenRealEstate')
string = string.replace('media_type', 'mediaType')

print(string)

# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class SimTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.wireless.v1.sims(sid="DEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://wireless.twilio.com/v1/Sims/DEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "unique_name",
                "commands_callback_method": "http_method",
                "commands_callback_url": "http://www.example.com",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "friendly_name": "friendly_name",
                "sms_fallback_method": "http_method",
                "sms_fallback_url": "http://www.example.com",
                "sms_method": "http_method",
                "sms_url": "http://www.example.com",
                "voice_fallback_method": "http_method",
                "voice_fallback_url": "http://www.example.com",
                "voice_method": "http_method",
                "voice_url": "http://www.example.com",
                "links": {
                    "data_sessions": "https://wireless.twilio.com/v1/Sims/DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/DataSessions",
                    "rate_plan": "https://wireless.twilio.com/v1/RatePlans/WPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "usage_records": "https://wireless.twilio.com/v1/Sims/DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UsageRecords"
                },
                "rate_plan_sid": "WPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "iccid": "iccid",
                "e_id": "e_id",
                "status": "new",
                "reset_status": null,
                "url": "https://wireless.twilio.com/v1/Sims/DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "ip_address": "192.168.1.1"
            }
            '''
        ))

        actual = self.client.wireless.v1.sims(sid="DEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.wireless.v1.sims.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://wireless.twilio.com/v1/Sims',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sims": [],
                "meta": {
                    "first_page_url": "https://wireless.twilio.com/v1/Sims?Status=new&Iccid=iccid&RatePlan=rate_plan&PageSize=50&Page=0",
                    "key": "sims",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://wireless.twilio.com/v1/Sims?Status=new&Iccid=iccid&RatePlan=rate_plan&PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.wireless.v1.sims.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sims": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "unique_name": "unique_name",
                        "commands_callback_method": "http_method",
                        "commands_callback_url": "http://www.example.com",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "friendly_name": "friendly_name",
                        "links": {
                            "data_sessions": "https://wireless.twilio.com/v1/Sims/DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/DataSessions",
                            "rate_plan": "https://wireless.twilio.com/v1/RatePlans/WPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                            "usage_records": "https://wireless.twilio.com/v1/Sims/DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UsageRecords"
                        },
                        "rate_plan_sid": "WPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "sid": "DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "iccid": "iccid",
                        "e_id": "e_id",
                        "status": "new",
                        "reset_status": "resetting",
                        "sms_fallback_method": "http_method",
                        "sms_fallback_url": "http://www.example.com",
                        "sms_method": "http_method",
                        "sms_url": "http://www.example.com",
                        "voice_fallback_method": "http_method",
                        "voice_fallback_url": "http://www.example.com",
                        "voice_method": "http_method",
                        "voice_url": "http://www.example.com",
                        "url": "https://wireless.twilio.com/v1/Sims/DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "ip_address": "192.168.1.30"
                    }
                ],
                "meta": {
                    "first_page_url": "https://wireless.twilio.com/v1/Sims?Status=new&Iccid=iccid&RatePlan=rate_plan&PageSize=50&Page=0",
                    "key": "sims",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://wireless.twilio.com/v1/Sims?Status=new&Iccid=iccid&RatePlan=rate_plan&PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.wireless.v1.sims.list()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.wireless.v1.sims(sid="DEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://wireless.twilio.com/v1/Sims/DEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "unique_name",
                "commands_callback_method": "http_method",
                "commands_callback_url": "http://www.example.com",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "friendly_name": "friendly_name",
                "links": {
                    "data_sessions": "https://wireless.twilio.com/v1/Sims/DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/DataSessions",
                    "rate_plan": "https://wireless.twilio.com/v1/RatePlans/WPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "usage_records": "https://wireless.twilio.com/v1/Sims/DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UsageRecords"
                },
                "rate_plan_sid": "WPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "iccid": "iccid",
                "e_id": "e_id",
                "status": "new",
                "reset_status": null,
                "sms_fallback_method": "http_method",
                "sms_fallback_url": "http://www.example.com",
                "sms_method": "http_method",
                "sms_url": "http://www.example.com",
                "voice_fallback_method": "http_method",
                "voice_fallback_url": "http://www.example.com",
                "voice_method": "http_method",
                "voice_url": "http://www.example.com",
                "url": "https://wireless.twilio.com/v1/Sims/DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "ip_address": "192.168.1.30"
            }
            '''
        ))

        actual = self.client.wireless.v1.sims(sid="DEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_update_move_to_subaccount_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
                "unique_name": "unique_name",
                "commands_callback_method": "http_method",
                "commands_callback_url": "http://www.example.com",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "friendly_name": "friendly_name",
                "links": {
                    "data_sessions": "https://wireless.twilio.com/v1/Sims/DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/DataSessions",
                    "rate_plan": "https://wireless.twilio.com/v1/RatePlans/WPbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
                    "usage_records": "https://wireless.twilio.com/v1/Sims/DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UsageRecords"
                },
                "rate_plan_sid": "WPbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
                "sid": "DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "iccid": "iccid",
                "e_id": "e_id",
                "status": "new",
                "reset_status": null,
                "sms_fallback_method": "http_method",
                "sms_fallback_url": "http://www.example.com",
                "sms_method": "http_method",
                "sms_url": "http://www.example.com",
                "voice_fallback_method": "http_method",
                "voice_fallback_url": "http://www.example.com",
                "voice_method": "http_method",
                "voice_url": "http://www.example.com",
                "url": "https://wireless.twilio.com/v1/Sims/DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "ip_address": "192.168.1.30"
            }
            '''
        ))

        actual = self.client.wireless.v1.sims(sid="DEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_update_reset_connectivity_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "unique_name",
                "commands_callback_method": "http_method",
                "commands_callback_url": "http://www.example.com",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "friendly_name": "friendly_name",
                "links": {
                    "data_sessions": "https://wireless.twilio.com/v1/Sims/DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/DataSessions",
                    "rate_plan": "https://wireless.twilio.com/v1/RatePlans/WPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "usage_records": "https://wireless.twilio.com/v1/Sims/DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UsageRecords"
                },
                "rate_plan_sid": "WPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "iccid": "iccid",
                "e_id": "e_id",
                "status": "active",
                "reset_status": "resetting",
                "sms_fallback_method": "http_method",
                "sms_fallback_url": "http://www.example.com",
                "sms_method": "http_method",
                "sms_url": "http://www.example.com",
                "voice_fallback_method": "http_method",
                "voice_fallback_url": "http://www.example.com",
                "voice_method": "http_method",
                "voice_url": "http://www.example.com",
                "url": "https://wireless.twilio.com/v1/Sims/DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "ip_address": "192.168.1.30"
            }
            '''
        ))

        actual = self.client.wireless.v1.sims(sid="DEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.wireless.v1.sims(sid="DEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://wireless.twilio.com/v1/Sims/DEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.wireless.v1.sims(sid="DEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

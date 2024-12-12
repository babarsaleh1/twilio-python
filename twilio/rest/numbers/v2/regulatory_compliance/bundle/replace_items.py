r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Numbers
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, Optional
from twilio.base import deserialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class ReplaceItemsInstance(InstanceResource):

    class Status(object):
        DRAFT = "draft"
        PENDING_REVIEW = "pending-review"
        IN_REVIEW = "in-review"
        TWILIO_REJECTED = "twilio-rejected"
        TWILIO_APPROVED = "twilio-approved"
        PROVISIONALLY_APPROVED = "provisionally-approved"

    """
    :ivar sid: The unique string that we created to identify the Bundle resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Bundle resource.
    :ivar regulation_sid: The unique string of a regulation that is associated to the Bundle resource.
    :ivar friendly_name: The string that you assigned to describe the resource.
    :ivar status: 
    :ivar valid_until: The date and time in GMT in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format when the resource will be valid until.
    :ivar email: The email address that will receive updates when the Bundle resource changes status.
    :ivar status_callback: The URL we call to inform your application of status changes.
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    def __init__(self, version: Version, payload: Dict[str, Any], bundle_sid: str):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.regulation_sid: Optional[str] = payload.get("regulation_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.status: Optional["ReplaceItemsInstance.Status"] = payload.get("status")
        self.valid_until: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("valid_until")
        )
        self.email: Optional[str] = payload.get("email")
        self.status_callback: Optional[str] = payload.get("status_callback")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )

        self._solution = {
            "bundle_sid": bundle_sid,
        }

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Numbers.V2.ReplaceItemsInstance {}>".format(context)


class ReplaceItemsList(ListResource):

    def __init__(self, version: Version, bundle_sid: str):
        """
        Initialize the ReplaceItemsList

        :param version: Version that contains the resource
        :param bundle_sid: The unique string that identifies the Bundle where the item assignments are going to be replaced.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "bundle_sid": bundle_sid,
        }
        self._uri = "/RegulatoryCompliance/Bundles/{bundle_sid}/ReplaceItems".format(
            **self._solution
        )

    def create(self, from_bundle_sid: str) -> ReplaceItemsInstance:
        """
        Create the ReplaceItemsInstance

        :param from_bundle_sid: The source bundle sid to copy the item assignments from.

        :returns: The created ReplaceItemsInstance
        """

        data = values.of(
            {
                "FromBundleSid": from_bundle_sid,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ReplaceItemsInstance(
            self._version, payload, bundle_sid=self._solution["bundle_sid"]
        )

    async def create_async(self, from_bundle_sid: str) -> ReplaceItemsInstance:
        """
        Asynchronously create the ReplaceItemsInstance

        :param from_bundle_sid: The source bundle sid to copy the item assignments from.

        :returns: The created ReplaceItemsInstance
        """

        data = values.of(
            {
                "FromBundleSid": from_bundle_sid,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ReplaceItemsInstance(
            self._version, payload, bundle_sid=self._solution["bundle_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Numbers.V2.ReplaceItemsList>"

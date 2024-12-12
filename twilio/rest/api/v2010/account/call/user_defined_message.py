r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, Optional, Union
from twilio.base import deserialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class UserDefinedMessageInstance(InstanceResource):
    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created User Defined Message.
    :ivar call_sid: The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the User Defined Message is associated with.
    :ivar sid: The SID that uniquely identifies this User Defined Message.
    :ivar date_created: The date that this User Defined Message was created, given in RFC 2822 format.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], account_sid: str, call_sid: str
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.call_sid: Optional[str] = payload.get("call_sid")
        self.sid: Optional[str] = payload.get("sid")
        self.date_created: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_created")
        )

        self._solution = {
            "account_sid": account_sid,
            "call_sid": call_sid,
        }

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.UserDefinedMessageInstance {}>".format(context)


class UserDefinedMessageList(ListResource):

    def __init__(self, version: Version, account_sid: str, call_sid: str):
        """
        Initialize the UserDefinedMessageList

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created User Defined Message.
        :param call_sid: The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the User Defined Message is associated with.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "call_sid": call_sid,
        }
        self._uri = (
            "/Accounts/{account_sid}/Calls/{call_sid}/UserDefinedMessages.json".format(
                **self._solution
            )
        )

    def create(
        self, content: str, idempotency_key: Union[str, object] = values.unset
    ) -> UserDefinedMessageInstance:
        """
        Create the UserDefinedMessageInstance

        :param content: The User Defined Message in the form of URL-encoded JSON string.
        :param idempotency_key: A unique string value to identify API call. This should be a unique string value per API call and can be a randomly generated.

        :returns: The created UserDefinedMessageInstance
        """

        data = values.of(
            {
                "Content": content,
                "IdempotencyKey": idempotency_key,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return UserDefinedMessageInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
        )

    async def create_async(
        self, content: str, idempotency_key: Union[str, object] = values.unset
    ) -> UserDefinedMessageInstance:
        """
        Asynchronously create the UserDefinedMessageInstance

        :param content: The User Defined Message in the form of URL-encoded JSON string.
        :param idempotency_key: A unique string value to identify API call. This should be a unique string value per API call and can be a randomly generated.

        :returns: The created UserDefinedMessageInstance
        """

        data = values.of(
            {
                "Content": content,
                "IdempotencyKey": idempotency_key,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return UserDefinedMessageInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.UserDefinedMessageList>"

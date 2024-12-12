r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Organization Public API
    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class AccountInstance(InstanceResource):
    """
    :ivar account_sid: Twilio account sid
    :ivar friendly_name: Account friendly name
    :ivar status: Account status
    :ivar owner_sid: Twilio account sid
    :ivar date_created: The date and time when the account was created in the system
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        organization_sid: Optional[str] = None,
        account_sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.status: Optional[str] = payload.get("status")
        self.owner_sid: Optional[str] = payload.get("owner_sid")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )

        self._solution = {
            "organization_sid": organization_sid or self.organization_sid,
            "account_sid": account_sid or self.account_sid,
        }
        self._context: Optional[AccountContext] = None

    @property
    def _proxy(self) -> "AccountContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AccountContext for this AccountInstance
        """
        if self._context is None:
            self._context = AccountContext(
                self._version,
                organization_sid=self._solution["organization_sid"],
                account_sid=self._solution["account_sid"],
            )
        return self._context

    def fetch(self) -> "AccountInstance":
        """
        Fetch the AccountInstance


        :returns: The fetched AccountInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "AccountInstance":
        """
        Asynchronous coroutine to fetch the AccountInstance


        :returns: The fetched AccountInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.PreviewIam.Organizations.AccountInstance {}>".format(context)


class AccountContext(InstanceContext):

    def __init__(self, version: Version, organization_sid: str, account_sid: str):
        """
        Initialize the AccountContext

        :param version: Version that contains the resource
        :param organization_sid:
        :param account_sid:
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "organization_sid": organization_sid,
            "account_sid": account_sid,
        }
        self._uri = "/{organization_sid}/Accounts/{account_sid}".format(
            **self._solution
        )

    def fetch(self) -> AccountInstance:
        """
        Fetch the AccountInstance


        :returns: The fetched AccountInstance
        """

        headers = values.of({})

        headers["Accept"] = "application/json"

        payload = self._version.fetch(method="GET", uri=self._uri, headers=headers)

        return AccountInstance(
            self._version,
            payload,
            organization_sid=self._solution["organization_sid"],
            account_sid=self._solution["account_sid"],
        )

    async def fetch_async(self) -> AccountInstance:
        """
        Asynchronous coroutine to fetch the AccountInstance


        :returns: The fetched AccountInstance
        """

        headers = values.of({})

        headers["Accept"] = "application/json"

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, headers=headers
        )

        return AccountInstance(
            self._version,
            payload,
            organization_sid=self._solution["organization_sid"],
            account_sid=self._solution["account_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.PreviewIam.Organizations.AccountContext {}>".format(context)


class AccountPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> AccountInstance:
        """
        Build an instance of AccountInstance

        :param payload: Payload response from the API
        """
        return AccountInstance(
            self._version, payload, organization_sid=self._solution["organization_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.PreviewIam.Organizations.AccountPage>"


class AccountList(ListResource):

    def __init__(self, version: Version, organization_sid: str):
        """
        Initialize the AccountList

        :param version: Version that contains the resource
        :param organization_sid:

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "organization_sid": organization_sid,
        }
        self._uri = "/{organization_sid}/Accounts".format(**self._solution)

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[AccountInstance]:
        """
        Streams AccountInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[AccountInstance]:
        """
        Asynchronously streams AccountInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AccountInstance]:
        """
        Lists AccountInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AccountInstance]:
        """
        Asynchronously lists AccountInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> AccountPage:
        """
        Retrieve a single page of AccountInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AccountInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Accept"] = "application/json"

        response = self._version.page(
            method="GET", uri=self._uri, params=data, headers=headers
        )
        return AccountPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> AccountPage:
        """
        Asynchronously retrieve a single page of AccountInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AccountInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Accept"] = "application/json"

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data, headers=headers
        )
        return AccountPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> AccountPage:
        """
        Retrieve a specific page of AccountInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AccountInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return AccountPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> AccountPage:
        """
        Asynchronously retrieve a specific page of AccountInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AccountInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return AccountPage(self._version, response, self._solution)

    def get(self, organization_sid: str, account_sid: str) -> AccountContext:
        """
        Constructs a AccountContext

        :param organization_sid:
        :param account_sid:
        """
        return AccountContext(
            self._version, organization_sid=organization_sid, account_sid=account_sid
        )

    def __call__(self, organization_sid: str, account_sid: str) -> AccountContext:
        """
        Constructs a AccountContext

        :param organization_sid:
        :param account_sid:
        """
        return AccountContext(
            self._version, organization_sid=organization_sid, account_sid=account_sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.PreviewIam.Organizations.AccountList>"

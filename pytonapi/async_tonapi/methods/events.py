from pytonapi.async_tonapi.client import AsyncTonapiClient
from pytonapi.schema.events import Event


class EventMethod(AsyncTonapiClient):

    async def get_event(self, event_id: str, accept_language: str = "en") -> Event:
        """
        Get an event either by event ID or a hash of any transaction in a trace.
        An event is built on top of a trace which is a series of transactions caused
        by one inbound message. TonAPI looks for known patterns inside the trace and
        splits the trace into actions, where a single action represents a meaningful
        high-level operation like a Jetton Transfer or an NFT Purchase.
        Actions are expected to be shown to users. It is advised not to build any logic
        on top of actions because actions can be changed at any time.

        :param event_id: event ID
        :param accept_language: Default value : en
        :return: :class:`Event`
        """
        method = f"v2/events/{event_id}"
        headers = {"Accept-Language": accept_language}
        response = await self._get(method=method, headers=headers)

        return Event(**response)

# Stubs for pika.adapters.blocking_connection (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from collections import namedtuple
from typing import Any, Optional

LOGGER: Any

class _CallbackResult:
    def __init__(self, value_class: Optional[Any] = ...) -> None: ...
    def reset(self) -> None: ...
    def __bool__(self): ...
    __nonzero__: Any = ...
    def __enter__(self): ...
    def __exit__(self, *args: Any, **kwargs: Any) -> None: ...
    def is_ready(self): ...
    @property
    def ready(self): ...
    def signal_once(self, *_args: Any, **_kwargs: Any) -> None: ...
    def set_value_once(self, *args: Any, **kwargs: Any) -> None: ...
    def append_element(self, *args: Any, **kwargs: Any) -> None: ...
    @property
    def value(self): ...
    @property
    def elements(self): ...

class _IoloopTimerContext:
    def __init__(self, duration: Any, connection: Any) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *_args: Any, **_kwargs: Any) -> None: ...
    def is_ready(self): ...

class _TimerEvt:
    timer_id: Any = ...
    def __init__(self, callback: Any) -> None: ...
    def dispatch(self) -> None: ...

class _ConnectionBlockedUnblockedEvtBase:
    def __init__(self, callback: Any, method_frame: Any) -> None: ...
    def dispatch(self) -> None: ...

class _ConnectionBlockedEvt(_ConnectionBlockedUnblockedEvtBase): ...
class _ConnectionUnblockedEvt(_ConnectionBlockedUnblockedEvtBase): ...

class BlockingConnection:

_OnOpenedArgs = namedtuple('BlockingConnection__OnOpenedArgs', 'connection')

_OnOpenErrorArgs = namedtuple('BlockingConnection__OnOpenErrorArgs', 'connection error')

_OnClosedArgs = namedtuple('BlockingConnection__OnClosedArgs', 'connection reason_code reason_text')

_OnChannelOpenedArgs = namedtuple('BlockingConnection__OnChannelOpenedArgs', 'channel')
    def __init__(self, parameters: Optional[Any] = ..., _impl_class: Optional[Any] = ...) -> None: ...
    def add_on_connection_blocked_callback(self, callback_method: Any) -> None: ...
    def add_on_connection_unblocked_callback(self, callback_method: Any) -> None: ...
    def add_timeout(self, deadline: Any, callback_method: Any): ...
    def add_callback_threadsafe(self, callback: Any) -> None: ...
    def remove_timeout(self, timeout_id: Any) -> None: ...
    def close(self, reply_code: int = ..., reply_text: str = ...) -> None: ...
    def process_data_events(self, time_limit: int = ...): ...
    def sleep(self, duration: Any) -> None: ...
    def channel(self, channel_number: Optional[Any] = ...): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, value: Any, traceback: Any) -> None: ...
    @property
    def is_closed(self): ...
    @property
    def is_closing(self): ...
    @property
    def is_open(self): ...
    @property
    def basic_nack_supported(self): ...
    @property
    def consumer_cancel_notify_supported(self): ...
    @property
    def exchange_exchange_bindings_supported(self): ...
    @property
    def publisher_confirms_supported(self): ...
    basic_nack: Any = ...
    consumer_cancel_notify: Any = ...
    exchange_exchange_bindings: Any = ...
    publisher_confirms: Any = ...

class _ChannelPendingEvt: ...

class _ConsumerDeliveryEvt(_ChannelPendingEvt):
    method: Any = ...
    properties: Any = ...
    body: Any = ...
    def __init__(self, method: Any, properties: Any, body: Any) -> None: ...

class _ConsumerCancellationEvt(_ChannelPendingEvt):
    method_frame: Any = ...
    def __init__(self, method_frame: Any) -> None: ...
    @property
    def method(self): ...

class _ReturnedMessageEvt(_ChannelPendingEvt):
    callback: Any = ...
    channel: Any = ...
    method: Any = ...
    properties: Any = ...
    body: Any = ...
    def __init__(self, callback: Any, channel: Any, method: Any, properties: Any, body: Any) -> None: ...
    def dispatch(self) -> None: ...

class ReturnedMessage:
    method: Any = ...
    properties: Any = ...
    body: Any = ...
    def __init__(self, method: Any, properties: Any, body: Any) -> None: ...

class _ConsumerInfo:
    SETTING_UP: int = ...
    ACTIVE: int = ...
    TEARING_DOWN: int = ...
    CANCELLED_BY_BROKER: int = ...
    consumer_tag: Any = ...
    no_ack: Any = ...
    consumer_cb: Any = ...
    alternate_event_sink: Any = ...
    state: Any = ...
    def __init__(self, consumer_tag: Any, no_ack: Any, consumer_cb: Optional[Any] = ..., alternate_event_sink: Optional[Any] = ...) -> None: ...
    @property
    def setting_up(self): ...
    @property
    def active(self): ...
    @property
    def tearing_down(self): ...
    @property
    def cancelled_by_broker(self): ...

class _QueueConsumerGeneratorInfo:
    params: Any = ...
    consumer_tag: Any = ...
    pending_events: Any = ...
    def __init__(self, params: Any, consumer_tag: Any) -> None: ...

class BlockingChannel:

_RxMessageArgs = namedtuple('BlockingChannel__RxMessageArgs', ['channel', 'method', 'properties', 'body'])

_MethodFrameCallbackResultArgs = namedtuple('BlockingChannel__MethodFrameCallbackResultArgs', 'method_frame')

_OnMessageConfirmationReportArgs = namedtuple('BlockingChannel__OnMessageConfirmationReportArgs', 'method_frame')

_OnChannelClosedByBrokerArgs = namedtuple('BlockingChannel__OnChannelClosedByBrokerArgs', 'method_frame')

_FlowOkCallbackResultArgs = namedtuple('BlockingChannel__FlowOkCallbackResultArgs', 'active')
    def __init__(self, channel_impl: Any, connection: Any) -> None: ...
    def __int__(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, value: Any, traceback: Any) -> None: ...
    @property
    def channel_number(self): ...
    @property
    def connection(self): ...
    @property
    def is_closed(self): ...
    @property
    def is_closing(self): ...
    @property
    def is_open(self): ...
    def close(self, reply_code: int = ..., reply_text: str = ...) -> None: ...
    def flow(self, active: Any): ...
    def add_on_cancel_callback(self, callback: Any) -> None: ...
    def add_on_return_callback(self, callback: Any): ...
    def basic_consume(self, consumer_callback: Any, queue: Any, no_ack: bool = ..., exclusive: bool = ..., consumer_tag: Optional[Any] = ..., arguments: Optional[Any] = ...): ...
    def basic_cancel(self, consumer_tag: Any): ...
    def start_consuming(self) -> None: ...
    def stop_consuming(self, consumer_tag: Optional[Any] = ...) -> None: ...
    def consume(self, queue: Any, no_ack: bool = ..., exclusive: bool = ..., arguments: Optional[Any] = ..., inactivity_timeout: Optional[Any] = ...) -> None: ...
    def get_waiting_message_count(self): ...
    def cancel(self): ...
    def basic_ack(self, delivery_tag: int = ..., multiple: bool = ...) -> None: ...
    def basic_nack(self, delivery_tag: Optional[Any] = ..., multiple: bool = ..., requeue: bool = ...) -> None: ...
    def basic_get(self, queue: Optional[Any] = ..., no_ack: bool = ...): ...
    def basic_publish(self, exchange: Any, routing_key: Any, body: Any, properties: Optional[Any] = ..., mandatory: bool = ..., immediate: bool = ...): ...
    def publish(self, exchange: Any, routing_key: Any, body: Any, properties: Optional[Any] = ..., mandatory: bool = ..., immediate: bool = ...) -> None: ...
    def basic_qos(self, prefetch_size: int = ..., prefetch_count: int = ..., all_channels: bool = ...) -> None: ...
    def basic_recover(self, requeue: bool = ...) -> None: ...
    def basic_reject(self, delivery_tag: Optional[Any] = ..., requeue: bool = ...) -> None: ...
    def confirm_delivery(self) -> None: ...
    def exchange_declare(self, exchange: Optional[Any] = ..., exchange_type: str = ..., passive: bool = ..., durable: bool = ..., auto_delete: bool = ..., internal: bool = ..., arguments: Optional[Any] = ...): ...
    def exchange_delete(self, exchange: Optional[Any] = ..., if_unused: bool = ...): ...
    def exchange_bind(self, destination: Optional[Any] = ..., source: Optional[Any] = ..., routing_key: str = ..., arguments: Optional[Any] = ...): ...
    def exchange_unbind(self, destination: Optional[Any] = ..., source: Optional[Any] = ..., routing_key: str = ..., arguments: Optional[Any] = ...): ...
    def queue_declare(self, queue: str = ..., passive: bool = ..., durable: bool = ..., exclusive: bool = ..., auto_delete: bool = ..., arguments: Optional[Any] = ...): ...
    def queue_delete(self, queue: str = ..., if_unused: bool = ..., if_empty: bool = ...): ...
    def queue_purge(self, queue: str = ...): ...
    def queue_bind(self, queue: Any, exchange: Any, routing_key: Optional[Any] = ..., arguments: Optional[Any] = ...): ...
    def queue_unbind(self, queue: str = ..., exchange: Optional[Any] = ..., routing_key: Optional[Any] = ..., arguments: Optional[Any] = ...): ...
    def tx_select(self): ...
    def tx_commit(self): ...
    def tx_rollback(self): ...

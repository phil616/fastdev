from contextvars import ContextVar
from fastapi import Request

def bind_contextvar(contextvar):
    class ContextVarBind:
        __slots__ = ()

        def __getattr__(self, name):
            return getattr(contextvar.get(), name)

        def __setattr__(self, name, value):
            setattr(contextvar.get(), name, value)

        def __delattr__(self, name):
            delattr(contextvar.get(), name)

        def __getitem__(self, index):
            return contextvar.get()[index]

        def __setitem__(self, index, value):
            contextvar.get()[index] = value

        def __delitem__(self, index):
            del contextvar.get()[index]

    return ContextVarBind()


async def bind_context_request(request: Request, call_next):
    """
    middleware for request
    bind the current request to context var
    """
    token = request_var.set(request)
    # log.debug(f"from {request.client.host}/{request.client.port} [ACCESSED] {request.url} " )
    try:
        response = await call_next(request)
        return response
    finally:
        request_var.reset(token)
    
request_var: ContextVar[Request] = ContextVar("request")
request: Request = bind_contextvar(request_var)
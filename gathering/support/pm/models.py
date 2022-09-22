from __future__ import annotations
from enum import Enum
from typing import Union, List, Any

from pydantic import Field
from qpyone.core.models import QBaseModel


class BaseEnum(Enum):
    @classmethod
    def has_value(cls, value):
        for enum in cls:
            if enum.value == value:
                return True
        return False


class RequestBodyMode(BaseEnum):
    RAW = "raw"
    URLENCODED = "urlencoded"
    FORMDATA = "formdata"
    FILE = "file"
    GRAPHQL = "graphql"


class VariableType(BaseEnum):
    STRING = "string"
    BOOLEAN = "boolean"
    ANY = "any"
    NUMBER = "number"


class AuthType(BaseEnum):
    APIKEY = "apikey"
    AWSV4 = "awsv4"
    BASIC = "basic"
    BEARER = "bearer"
    DIGEST = "digest"
    EDGEGRID = "edgegrid"
    HAWK = "hawk"
    NOAUTH = "noauth"
    OAUTH1 = "oauth1"
    OAUTH2 = "oauth2"
    NTLM = "ntlm"


class Description(QBaseModel):
    content: str = ""
    desc_type: str = ""
    version: str = ""


class Version(QBaseModel):
    major: str = ""
    minor: str = ""
    patch: str = ""
    identifier: str = ""


class Info(QBaseModel):
    name: str = ""
    pm_schema: str = Field(default=None, alias="schema")
    postman_id: str = ""
    description: Union[Description, str, None] = None
    version: Union[Version, str, None] = None


class CertificateKey(QBaseModel):
    src: str = None


class Certificate(QBaseModel):
    name: str = ""
    matches: List[str] = None
    key: CertificateKey = ""
    passphrase: str = ""


class AuthAttribute(QBaseModel):
    key: str = None
    value: Any = None
    auth_attr_type: str = ""


class Auth(QBaseModel):
    auth_type: str = None
    no_auth: Any = None
    apikey: List[AuthAttribute] = None
    awsv4: List[AuthAttribute] = None
    basic: List[AuthAttribute] = None
    bearer: List[AuthAttribute] = None
    digest: List[AuthAttribute] = None
    edgegrid: List[AuthAttribute] = None
    hawk: List[AuthAttribute] = None
    noauth: List[AuthAttribute] = None
    oauth1: List[AuthAttribute] = None
    oauth2: List[AuthAttribute] = None
    ntlm: List[AuthAttribute] = None


class Cookie(QBaseModel):
    domain: str = None
    path: str = None
    expires: Union[str, None] = None
    max_age: str = ""
    host_only: bool = False
    http_only: bool = False
    name: str = ""
    secure: bool = False
    session: bool = False
    value: str = ""
    extensions: List = None


class KeyVal(QBaseModel):
    key: str = None
    value: str = None
    disabled: bool = False
    description: Union[Description, None, str] = None


class Variable(QBaseModel):
    id: str = None
    key: str = None
    value: Union[str, bool, int, Any] = None
    variable_type: str = "any"
    name: str = ""
    description: Description = None
    system: bool = False


class Url(QBaseModel):
    raw: str = None
    protocol: str = None
    port: str = None
    host: Union[str, List[str]] = ""
    path: Union[str, List[str]] = ""
    query: List[KeyVal] = None
    url_hash: str = ""
    variable: List[Variable] = None


class Script(QBaseModel):
    id: str = ""
    script_type: str = ""
    script_exec: Union[List[str], str] = ""
    src: Url = None
    name: str = ""


class Request(QBaseModel):
    url: Union[Url, str] = None
    method: str = None
    auth: Auth = None
    proxy: ProxyConfig = None
    certificate: Certificate = None
    header: Union[List[KeyVal], str] = ""
    body: Union[RequestBody, None, Any] = None
    description: Description = None


class RequestBody(QBaseModel):
    mode: str = None  # [raw, urlencoded, formdata, file, graphql]
    raw: str = ""
    urlencoded: List[KeyVal] = None
    graphql: dict = None
    formdata: Union[List[FormParameter]] = None
    request_body_file: Union[RequestBodyFile, None] = None
    options: dict = None
    disabled: bool = False


class RequestBodyFile(QBaseModel):
    src: Union[str, None] = None
    content: str = ""


class Response(QBaseModel):
    id: str = ""
    original_request: Request = None
    response_time: Union[str, int, None] = None
    timings: Union[dict, None] = None
    header: Union[List[Union[KeyVal, str]], str, None] = None
    cookie: Union[List[Cookie], None] = None
    body: Union[str, None] = None
    status: str = ""
    code: int = 0


class ProxyConfig(QBaseModel):
    match: str = "http+https://*/*"
    host: str = ""
    port: int = 8080
    tunnel: bool = False
    disabled: bool = False

    def get_proxy_url(self):
        return f"{self.host}:{self.port}"


class FormParameter(QBaseModel):
    key: str = None
    value: str = ""
    src: Union[List, str, None] = None
    disabled: bool = False
    form_param_type: str = ""
    content_type: str = ""  # should override content-type in header
    description: Union[Description, None, str] = None


class Event(QBaseModel):
    listen: str = None
    id: str = ""
    script: Script = None
    disabled: bool = False


class Item(QBaseModel):
    """
    Corresponds to single API endpoint
    """

    request: Union[Request, str] = None
    id: str = ""
    name: str = ""
    description: Union[Description, str, None] = None
    response: List[Response] = None
    event: List[Event] = None


class ItemGroup(QBaseModel):
    item: List[Union[Item, ItemGroup]] = None
    name: str = ""
    description: Description = None
    variable: Variable = None
    auth: Auth = None
    event: List[Event] = None


Request.update_forward_refs()


class PostmanCollection(QBaseModel):
    file_path: str = ""
    variable: List[Variable] = None
    auth: Auth = None
    info: Info = None
    item: List[Union[Item, ItemGroup]] = None
    event: List[Event] = None


class SimplePostmanCollection(QBaseModel):
    """
    TODO: to simplify the postman model
    """
    pass

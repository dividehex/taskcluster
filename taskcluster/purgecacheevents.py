# coding=utf-8
#####################################################
# THIS FILE IS AUTOMATICALLY GENERATED. DO NOT EDIT #
#####################################################
# noqa: E128,E201
from .client import BaseClient
from .client import createApiClient
from .client import config
from .client import createTemporaryCredentials
from .client import createSession
_defaultConfig = config


class PurgeCacheEvents(BaseClient):
    """
    The purge-cache service, typically available at
    `purge-cache.taskcluster.net`, is responsible for publishing a pulse
    message for workers, so they can purge cache upon request.

    This document describes the exchange offered for workers by the
    cache-purge service.
    """

    classOptions = {
        "exchangePrefix": "exchange/taskcluster-purge-cache/v1/"
    }

    """
    Purge Cache Messages

    When a cache purge is requested  a message will be posted on this
    exchange with designated `provisionerId` and `workerType` in the
    routing-key and the name of the `cacheFolder` as payload

    This exchange outputs: ``http://schemas.taskcluster.net/purge-cache/v1/purge-cache-message.json#``This exchange takes the following keys:

     * routingKeyKind: Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key. (required)

     * provisionerId: `provisionerId` under which to purge cache. (required)

     * workerType: `workerType` for which to purge cache. (required)
    """

    def purgeCache(self, *args, **kwargs):
        return self._makeTopicExchange({'routingKey': [{'required': True, 'multipleWords': False, 'summary': "Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key.", 'name': 'routingKeyKind', 'constant': 'primary'}, {'required': True, 'multipleWords': False, 'summary': '`provisionerId` under which to purge cache.', 'name': 'provisionerId'}, {'required': True, 'multipleWords': False, 'summary': '`workerType` for which to purge cache.', 'name': 'workerType'}], 'name': 'purgeCache', 'schema': 'http://schemas.taskcluster.net/purge-cache/v1/purge-cache-message.json#', 'exchange': 'purge-cache'}, *args, **kwargs)

    funcinfo = {
    }


__all__ = ['createTemporaryCredentials', 'config', '_defaultConfig', 'createApiClient', 'createSession', 'PurgeCacheEvents']

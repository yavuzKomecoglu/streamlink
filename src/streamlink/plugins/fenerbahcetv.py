import re
import logging

from streamlink.plugin import Plugin
from streamlink.plugin.api.utils import itertags
from streamlink.plugins.dailymotion import DailyMotion
from streamlink.stream import HLSStream
from streamlink.utils import update_scheme

log = logging.getLogger(__name__)


class FenerbahceTV(Plugin):
    """
    Support for Fenerbahce TV live stream: https://www.fenerbahce.org/fbtv/
    """

    url_re = re.compile(r"""
        https?://(?:www.)?
        (?:fenerbahce.org/fbtv/.*)
    """, re.VERBOSE)

    @classmethod
    def can_handle_url(cls, url):
        return cls.url_re.match(url) is not None

    def _get_streams(self):
        res = self.session.http.get(self.url)

        # Look for Youtube embedded video first
        for iframe in itertags(res.text, 'iframe'):            
            if 'dailymotion' in iframe.attributes.get("src"):
                dailymotion_embed_src = iframe.attributes.get("src").replace("//www.dailymotion.com","https://www.dailymotion.com")
                if DailyMotion.can_handle_url(dailymotion_embed_src):
                    log.debug("Handing off to DailyMotion plugin")
                    return self.session.streams(dailymotion_embed_src)

__plugin__ = FenerbahceTV

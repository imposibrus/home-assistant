from aiohttp import web
from homeassistant.components.http import HomeAssistantView

DOMAIN = "test"

async def async_setup(hass, config):
    url_set = hass.data['frontend_extra_module_url']
    url_set.add('/test.js')
    hass.http.register_view(ModView(hass, '/test.js'))

    return True


class ModView(HomeAssistantView):

    name = "test_script"
    requires_auth = False

    def __init__(self, hass, url):
        self.url = url
        self.config_dir = hass.config.path()

    async def get(self, request):
        path = "{}/custom_components/test/test.js".format(self.config_dir)

        filecontent = ""

        try:
            with open(path, mode="r", encoding="utf-8", errors="ignore") as localfile:
                filecontent = localfile.read()
                localfile.close()
        except Exception:
            pass

        return web.Response(
            body=filecontent, content_type="text/javascript", charset="utf-8"
        )


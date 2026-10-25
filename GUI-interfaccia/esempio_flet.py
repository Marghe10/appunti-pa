import asyncio

import flet as ft

async def main(page:ft.Page):
    il_mio_testo = ft.Text("questo è il mio primo testo!!!", size=24, color="blue")
    page.controls.append(il_mio_testo)
    page.update()

    for i in range (1,100):
        il_mio_testo.value=f"{i}"
        il_mio_testo.update()
        await asyncio.sleep(1)
        page.update()

ft.run(main)
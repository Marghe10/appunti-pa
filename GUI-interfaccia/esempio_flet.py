import asyncio

import flet as ft

async def main(page:ft.Page):
    il_mio_testo = ft.Text("questo è il mio primo testo!!!", size=24, color="blue")
    page.controls.append(il_mio_testo)

    for i in range (1,100):
        il_mio_testo.value=f"{i}"
        await asyncio.sleep(1)
        il_mio_testo.update()
    page.update()


ft.run(main)
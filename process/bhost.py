# This hosts main singleton obj


import process.bavanga as bavanga
from process.queue import TQueue


g_bavanga = bavanga.Bavanga(None)
g_queue = TQueue()
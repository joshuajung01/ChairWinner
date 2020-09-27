async def amazon_search(ctx, query):
    await ctx.send(f'Searching Amazon for "{query}"...')
    # code here to do the actual searching
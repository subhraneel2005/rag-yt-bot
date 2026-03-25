def chunk_transcript(transcript, chunk_size, overlap):
    chunks = []
    words = []

    # current_start = transcript[0].start

    for snip in transcript:
        snip_words = snip['text'].split()
        snip_start = snip['start']
        snip_end = snip['end']
        word_count = len(snip_words)

        for  i, word in enumerate(snip_words):

             # Interpolate timestamp per word within the snippet
            estimated_time = snip_start + (i / max(word_count, 1)) * (snip_end - snip_start)
            words.append((word, estimated_time, snip_end))
        

            if(len(words) >= chunk_size):

                chunk_text = ' '.join([word for word, _, _ in words])
                chunk_start = words[0][1]
                chunk_end = words[-1][2]

                chunks.append({
                    "text": chunk_text,
                    "start_time": round(chunk_start, 3),
                    "end_time": round(chunk_end, 3)
                })

                # slide window
                overlap_words = int(chunk_size * overlap)
                words = words[chunk_size - overlap_words:]  # slide forward, keep overlap
    
       # handle remaining words
    if words:
        chunk_text = ' '.join([word for word, _, _ in words])
        chunk_start = words[0][1]
        chunk_end = words[-1][2]
        chunks.append({
            'text': chunk_text,
            'start_time': round(words[0][1], 3),
            'end_time': round(words[-1][2], 3)
        })

    print("-------CHUNKS-------")
    print(chunks)
    print("total chunks length", len(chunks))
    return chunks
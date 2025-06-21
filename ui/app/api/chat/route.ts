import { NextResponse } from 'next/server';

const API_URL = process.env.API_URL;

export async function GET() {
  console.log('[API/chat] Trying:', `${API_URL}/chat`);

  try {
    const res = await fetch(`${API_URL}/chat`);
    const text = await res.text();

    console.log('[API/chat] Response text:', text);
    console.log('[API/chat] Status:', res.status);

    return NextResponse.json(JSON.parse(text));
  } catch (e) {
    console.error('[API/chat] Fetch failed:', e);
    return NextResponse.json({ error: 'Connection failed' }, { status: 502 });
  }
}

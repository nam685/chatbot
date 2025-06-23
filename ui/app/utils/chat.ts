export async function fetchThreads() {
  const res = await fetch(`/api/chat`);
  return res.json();
}

export async function deleteThread(threadId: string) {
  const res = await fetch(`/api/chat/${threadId}`, {
    method: 'DELETE',
  });
  return res.json();
}

export async function sendMessage(threadId: string, message: string) {
  const res = await fetch(`/api/chat/${threadId}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ text: message }),
  });
  return res.json();
}

export async function sendHumanReview(
  threadId: string,
  review: { action: string; data: string }
) {
  const res = await fetch(`/api/chat/${threadId}/human_review`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(review),
  });
  return res.json();
}

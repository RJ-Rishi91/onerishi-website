import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context: any) {
  const API_URL = import.meta.env.PUBLIC_API_URL || process.env.PUBLIC_API_URL || 'https://onerishi-website.onrender.com';
  let items: any[] = [];

  try {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 20000);
    const res = await fetch(`${API_URL}/api/posts`, { signal: controller.signal });
    clearTimeout(timeoutId);
    if (res.ok) {
      const apiPosts = await res.json();
      if (Array.isArray(apiPosts) && apiPosts.length > 0) {
        items = apiPosts.map((p) => ({
          title: p.title,
          pubDate: p.published_at ? new Date(p.published_at) : new Date(),
          description: p.excerpt,
          link: `/writing/${p.slug}/`,
        }));
      }
    }
  } catch {
    // Fallback
  }

  if (items.length === 0) {
    const posts = await getCollection('writing');
    items = posts.map((post) => ({
      title: post.data.title,
      pubDate: new Date(post.data.date),
      description: post.data.description,
      link: `/writing/${post.slug}/`,
    }));
  }

  return rss({
    title: 'OneRishi.in — Dispatches & Field Notes',
    description: 'Real experiments, field notes, and frameworks from marketing, technology, and building on the internet by Rushal Sharma.',
    site: context.site || 'https://onerishi.in',
    items,
    customData: `<language>en-us</language>`,
  });
}

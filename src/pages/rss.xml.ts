import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context: any) {
  const posts = await getCollection('writing');
  return rss({
    title: 'OneRishi.in — Dispatches & Field Notes',
    description: 'Real experiments, field notes, and frameworks from marketing, technology, and building on the internet by Rushal S.',
    site: context.site || 'https://onerishi.in',
    items: posts.map((post) => ({
      title: post.data.title,
      pubDate: new Date(post.data.date),
      description: post.data.description,
      link: `/writing/${post.slug}/`,
    })),
    customData: `<language>en-us</language>`,
  });
}

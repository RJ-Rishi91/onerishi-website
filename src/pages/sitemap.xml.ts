import { getCollection } from 'astro:content';

export async function GET(context: any) {
  const siteUrl = context.site?.toString().replace(/\/$/, '') || 'https://onerishi.in';

  const staticPages = [
    '',
    'work',
    'writing',
    'about',
    'labs',
    'philosophy',
    'impact',
    'collaborate',
    'contact',
  ];

  const workEntries = await getCollection('work');
  const writingEntries = await getCollection('writing');

  const urls: Array<{ loc: string; lastmod?: string; changefreq: string; priority: string }> = [];

  // Static routes
  staticPages.forEach((page) => {
    urls.push({
      loc: page ? `${siteUrl}/${page}` : siteUrl,
      changefreq: page === '' ? 'weekly' : 'monthly',
      priority: page === '' ? '1.0' : '0.8',
    });
  });

  // Dynamic Case Studies
  workEntries.forEach((entry) => {
    urls.push({
      loc: `${siteUrl}/work/${entry.slug}`,
      changefreq: 'monthly',
      priority: '0.8',
    });
  });

  // Dynamic Writing Essays
  writingEntries.forEach((post) => {
    urls.push({
      loc: `${siteUrl}/writing/${post.slug}`,
      lastmod: new Date(post.data.date).toISOString().split('T')[0],
      changefreq: 'monthly',
      priority: '0.7',
    });
  });

  const sitemapXml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls
  .map(
    (u) => `  <url>
    <loc>${u.loc}</loc>
    ${u.lastmod ? `<lastmod>${u.lastmod}</lastmod>` : ''}
    <changefreq>${u.changefreq}</changefreq>
    <priority>${u.priority}</priority>
  </url>`
  )
  .join('\n')}
</urlset>`;

  return new Response(sitemapXml, {
    headers: {
      'Content-Type': 'application/xml; charset=utf-8',
    },
  });
}

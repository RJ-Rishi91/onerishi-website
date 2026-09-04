import { defineCollection, z } from 'astro:content';

const workCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    role: z.string(),
    timeframe: z.string(),
    location: z.string(),
    scale: z.string(),
    categoryTag: z.string(),
    caseNumber: z.string(),
    order: z.number().default(1),
    metrics: z.array(
      z.object({
        label: z.string(),
        value: z.string(),
      })
    ).optional(),
    operationalStack: z.array(z.string()).optional(),
    heroImage: z.string().optional(),
    heroImageAlt: z.string().optional(),
    heroCaption: z.string().optional(),
    nextSlug: z.string().optional(),
    nextTitle: z.string().optional(),
    prevSlug: z.string().optional(),
    prevTitle: z.string().optional(),
  }),
});

const writingCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    category: z.enum([
      'Marketing Experiments',
      'Marketing × Tech',
      'Building on the Internet',
      'Projects & Behind-the-Scenes',
      'Career & Learning',
    ]),
    date: z.string(),
    readTime: z.string(),
    volume: z.string().default('Vol. 04'),
    featured: z.boolean().default(false),
    coverImage: z.string().optional(),
    coverImageAlt: z.string().optional(),
    coverCaption: z.string().optional(),
    writtenFromExperience: z.object({
      title: z.string(),
      note: z.string(),
    }).optional(),
    relatedSlugs: z.array(z.string()).optional(),
  }),
});

export const collections = {
  work: workCollection,
  writing: writingCollection,
};

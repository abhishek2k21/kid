export type FetchStatus = 'resolved' | 'unresolved';

export interface InstagramItem {
  shortcode: string;
  kind: 'reel' | 'post';
  url: string; // tracking params stripped
  originalUrl: string;
  status: FetchStatus;
  statusReason: string | null;
  title: string | null;
  author: string | null;
  topics: string[];
}

export interface GithubRepo {
  fullName: string;
  url: string;
  description: string;
  license: string | null;
  stars: string; // as displayed on GitHub at fetch time
  forks: string;
  topics: string[];
  homepage: string | null;
  category: string;
  notes: string[];
}

export interface SkillItem {
  name: string;
  status: 'unverified';
  notes: string;
}

export interface Dataset {
  fetchedAt: string;
  instagram: InstagramItem[];
  github: GithubRepo[];
  skills: SkillItem[];
}

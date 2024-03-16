export interface Product {
  id: number;
  category: string;
  cover: string;
  images: string[];
  created?: string;
  description?: string;
  owner: string;
  price: number;
  status: string;
  tags: string[];
  title: string;
  updated?: string;
}

export interface Category {
  id: number;
  name: string;
}

export interface Tag {
  id: number;
  name: string;
}

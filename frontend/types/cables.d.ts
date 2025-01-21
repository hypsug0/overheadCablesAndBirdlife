import type { Geometry } from "geojson";
import type { Nomenclature } from "./nomenclature";

export interface Media {
  author?: string | null;
  date: string | Date ;
  id?: number;
  remark?: string | null;
  source?: string | null;
  storage: string | null;
}

export interface DiagData {
  id?: number | null;
  date: string | Date;
  remark: string | null;
  technical_proposal: string | null;
  infrastructure: number | null;
  pole_type_id: Array<number>;
  neutralized: boolean;
  condition_id: number | null;
  attraction_advice: boolean;
  dissuasion_advice: boolean;
  isolation_advice: boolean;
  pole_attractivity_id?: number | null;
  pole_dangerousness_id?: number | null;
  sgmt_moving_risk_id?: number | null;
  sgmt_topo_integr_risk_id?: number | null;
  sgmt_landscape_integr_risk_id?: number | null;
  media_id: Array<number>;
}

export type Diagnosis = DiagData & {
  change_advice?: boolean;
  infrastructure?: number;
  last?: boolean;
  media: Media[];
  condition: Nomenclature;
  pole_attractivity: Nomenclature;
  pole_dangerousness: Nomenclature;
  pole_type: Nomenclature[];
  sgmt_build_integr_risk: Nomenclature;
  sgmt_moving_risk: Nomenclature;
  sgmt_topo_integr_risk: Nomenclature;
  sgmt_veget_integr_risk: Nomenclature;
  sgmt_landscape_integr_risk: Nomenclature;
};

export type InfrastructurePolymorphic = {
  created_by: any | null;
  geo_area?: any;
  id: number;
  owner: any;
  polymorphic_ctype: any | null;
  sensitive_area?: any;
  timestamp_create: string;
  timestamp_update: string;
  updated_by: any | null;
  uuid: string;
};

export type GeoArea = {
  code: string;
  id: number;
  name: string;
  type: Nomenclature;
};

export interface Equipment {
  comment: string | null;
  count: number;
  reference: string | null;
  type?: Nomenclature[];
  type_id?: number;
}

export type Operation = {
  date?: string;
  equipments: Equipment[];
  id: number;
  infrastructure: number;
  last?: boolean;
  media: Media[];
  media_id?: number[];
  remark?: string | null;
};

export type SensitiveArea = {
  code: string;
  id: number;
  name: string;
};

export type Line = {
  diagnosis: Diagnosis[];
  geo_area: GeoArea[];
  geom?: Geometry | null;
  id: number;
  operations: Operation[];
  owner: Nomenclature;
  owner_id: any;
  sensitive_area: SensitiveArea[];
};

export type OperationPolymorphic = {
  created_by: any | null;
  date?: string;
  equipments?: any;
  id: number;
  infrastructure: any;
  last?: boolean;
  media?: any;
  polymorphic_ctype: any | null;
  remark?: string | null;
  timestamp_create: string;
  timestamp_update: string;
  updated_by: any | null;
  uuid: string;
};

export type Point = {
  diagnosis: Diagnosis[];
  geo_area: GeoArea[];
  geom?: Geometry | null;
  id: number;
  operations: Operation[];
  owner: Nomenclature;
  owner_id: any;
  sensitive_area: SensitiveArea[];
};

export type Infrastructure = {
  diagnosis: Diagnosis[];
  geo_area: GeoArea[];
  geom?: Geometry | null;
  id: number;
  operations: Operation[];
  owner: Nomenclature;
  owner_id: any;
  sensitive_area: SensitiveArea[];
};

export interface CablesFeature extends Feature {
  properties?: {
    resource_type?: string; // Optional key for resource type
    [key: string]: any; // Allow other properties
  };
}

export type CablesFeatureCollection = FeatureCollection<CablesFeature>;

export interface Risk {
  note: number;
  label: string;
  color: string;
}
